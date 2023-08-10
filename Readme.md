
# Projeto: Divisão e Reconstrução de Arquivos Usando QR Codes

Este projeto fornece uma ferramenta para dividir um arquivo em vários códigos QR e, posteriormente, reconstruir o arquivo original a partir desses códigos QR.

## Pré-requisitos

- Python
- Bibliotecas Python:
  - `qrcode`
  - `pyzbar`
  - `PIL` (Pillow)

Instale as bibliotecas necessárias usando:

```bash
pip install -r requirements.txt
```

## Uso

O script fornece dois modos de operação:

1. **Modo "split"**: Para dividir um arquivo em QR Codes.
2. **Modo "rebuild"**: Para reconstruir um arquivo a partir dos QR Codes.

### Dividir um arquivo em QR Codes:

```bash
python main.py split nome_do_arquivo.extensao
```

Este comando irá criar imagens QR Code no diretório "qrcodes".

### Reconstruir o arquivo a partir dos QR Codes:

```bash
python main.py rebuild nome_do_arquivo_reconstruido.extensao
```

## Código

O código principal é dividido em duas funções principais:

- `split_file_into_qrcodes(filename)`: Divide o arquivo especificado em vários códigos QR.
- `rebuild_file_from_qrcodes(output_filename)`: Reconstrói o arquivo original a partir das imagens de QR Code no diretório "qrcodes".
