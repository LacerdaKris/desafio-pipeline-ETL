import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

file_path = 'mensagens.csv'
encoding = detect_encoding(file_path)
print(f"A codificação do arquivo é: {encoding}")