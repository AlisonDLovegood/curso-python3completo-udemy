frase = "Stay with me mayonakano doa o tataki kaeranaide to naita ano kisetsu ga ima me no mae"

i = 0
letra = ""
contagem = 0
while i < len(frase):
    letra_atual = frase[i]
    contagem_atual = frase.count(letra_atual)

    if contagem_atual > contagem and letra_atual != " ":
        contagem = contagem_atual
        letra = letra_atual

    i = i + 1
print(f'A letra com maior frequencia foi {letra}, aparecendo {contagem} vezes.')