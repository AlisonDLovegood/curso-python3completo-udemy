"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        v Seu nome é {nome}
        v Seu nome invertido é {nome invertido}
        v Seu nome contém (ou não) espaços
        v Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
print(50*"=")
print(f'{" ENTRADAS ":-^50}')
nome = input("Digite o seu nome: ")
idade = input("Digite o sua idade: ")
print(f'{" SAIDAS ":-^50}')
if (nome != "") and (idade != ""):
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if " " in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

elif nome == "":
    print("Você não preencheu o campo obrigatório do nome!")
else:
    print("Você não preencheu o campo obrigatório da idade!")
