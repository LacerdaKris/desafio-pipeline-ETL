import json
import pandas
import random

# abrindo o arquivo JSON com os pets cadastrados na petshop
with open("pets.json", "r") as file:
    dados = json.load(file)

# lendo as mensagens cadastradas no csv e incluindo numa lista
db = pandas.read_csv("mensagens.csv", encoding="ascii", header=None)
mensagens = db[0].tolist()


# escolhe uma das mensagens do arquivo csv aleatoriamente
def AtribuirMensagem():
    mensagem_escolhida = random.choice(mensagens)
    return mensagem_escolhida


# atribui uma mensagem a cada pet
for pet in dados:
    news = AtribuirMensagem()
    id_atual = pet["news"][-1]["id"]
    nome_pet = pet["name"]
    formato = f"Recado aos pais do pet: {nome_pet}...\n {news}"
    pet["news"].append({"id": id_atual + 1, "type": "new", "description": formato})

#altera o arquivo json com a inclusão da mensagem
with open("pets.json", "w") as file:
    result = json.dump(dados, file, indent=4)

if result is None:
    print("A gravação em 'pets.json' foi bem-sucedida.")
else:
    print("Erro ao gravar em 'pets.json'.")
