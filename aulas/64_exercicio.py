nome = "Alison Lovegood"
nome_modificado = ""
tamanho = len(nome)
aux = 0
while aux < tamanho:
    letra = nome[aux]
    nome_modificado += f'*{letra}'
    # nome_modificado += "*"+letra
    aux += 1
nome_modificado += "*"
print(nome_modificado)