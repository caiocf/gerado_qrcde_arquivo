import base64
import os
import qrcode
import sys
from PIL import Image
from pyzbar.pyzbar import decode as qr_decode

CHUNK_SIZE = 2953  # Ajustado para o tamanho máximo de bytes para QR Code versão 40 com correção de erros "L"


def split_file_into_qrcodes(filename):
    # Verificando se o diretório 'qrcodes' existe, senão, cria-o
    if not os.path.exists('qrcodes'):
        os.makedirs('qrcodes')

    # Lendo e codificando o arquivo em Base64
    with open(filename, 'rb') as f:
        encoded_content = base64.b64encode(f.read()).decode('utf-8')

    # Dividindo o conteúdo codificado em chunks
    chunks = [encoded_content[i:i + CHUNK_SIZE] for i in range(0, len(encoded_content), CHUNK_SIZE)]

    # Convertendo cada chunk em um QR Code e salvando como imagem
    for index, chunk in enumerate(chunks):
        qr = qrcode.QRCode(
            version=40,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(chunk)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'qrcodes/{index}.png')
    print(f"{len(chunks)} QR codes gerados e salvos na pasta 'qrcodes'.")
    print("Para reconstruir o conteúdo, use o modo 'rebuild'.")



def rebuild_file_from_qrcodes(output_filename):
    # Listando todas as imagens no diretório 'qrcodes'
    files = sorted(os.listdir('qrcodes'), key=lambda x: int(x.split('.')[0]))

    combined_base64 = ""

    # Decodificando o conteúdo de cada QR Code usando pyzbar
    for file in files:
        with Image.open(f'qrcodes/{file}') as img:
            decoded_data = qr_decode(img)
            combined_base64 += decoded_data[0].data.decode('utf-8')

    # Decodificando a string Base64 combinada
    decoded_content = base64.b64decode(combined_base64)

    # Salvando o conteúdo reconstruído como um novo arquivo
    with open(output_filename, 'wb') as f:
        f.write(decoded_content)
    print(f"Conteúdo reconstruído com sucesso e salvo como {output_filename}.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python script_name.py [split|rebuild] nome_do_arquivo.extensao")
        sys.exit(1)

    mode = sys.argv[1]
    filename = sys.argv[2]

    if mode == "split":
        split_file_into_qrcodes(filename)
    elif mode == "rebuild":
        rebuild_file_from_qrcodes(filename)
        print(f'Tamanho do arquivo reconstruído: {os.path.getsize(filename)} bytes')
    else:
        print("Modo inválido. Use 'split' ou 'rebuild'.")
        sys.exit(1)
