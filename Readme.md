# Projeto de Divisão e Reconstrução de Arquivos Usando QR Codes

Este projeto oferece uma ferramenta robusta para **divisão de arquivos** e **reconstrução** usando **QR Codes**. Ele permite que os usuários codifiquem arquivos em múltiplos códigos QR e, posteriormente, decodifiquem esses códigos QR para reconstruir o arquivo original.

## Recursos

- **Divisão de Arquivos**: Converta rapidamente qualquer arquivo em uma série de imagens QR Code.
- **Reconstrução de Arquivos**: Decodifique uma série de imagens QR Code para reconstruir o arquivo original.
- **Backup de Arquivos**: Use QR Codes como uma forma alternativa de backup de arquivos.
- **Leitura de QR Code**: Decodifique facilmente QR Codes para extrair informações do arquivo.

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

## Como Usar

O script fornece dois modos de operação:

1. **Modo "split"**: Para dividir um arquivo em QR Codes.
2. **Modo "rebuild"**: Para reconstruir um arquivo a partir dos QR Codes.

### Dividir um arquivo em QR Codes:

```bash
python main.py split meu_arquivo.zip
```

Este comando irá criar imagens QR Code no diretório "qrcodes".

### Reconstruir o arquivo a partir dos QR Codes:

```bash
python main.py rebuild meu_arquivo_remontado.zip
```

## FAQ (Perguntas Frequentes)

**Q: O que é a vantagem de usar QR Codes para divisão de arquivos?**  
A: Usar QR Codes para dividir arquivos oferece uma maneira visual e física de armazenar dados, o que pode ser útil para backups físicos ou compartilhamento rápido.

**Q: Posso usar este projeto para backup de arquivos grandes?**  
A: Sim, mas lembre-se de que arquivos muito grandes resultarão em um grande número de QR Codes.

## Contribuições

Estamos abertos a contribuições! Se você tiver melhorias, correções ou novos recursos, sinta-se à vontade para abrir um pull request.

---

Você pode fazer o download deste `README.md` revisado e adicioná-lo ao seu repositório. Se você tiver mais ajustes ou perguntas, estou aqui para ajudar!