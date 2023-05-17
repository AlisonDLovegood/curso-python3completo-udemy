"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print(50*"=")
print(f'{" ENTRADA ":-^50}')
ok = True

# PRIMEIRO
# while ok:
#     try:
#         numero = int(input('Digite um número inteiro: '))
#         ok = False
#     except:
#         print('Não é um número inteiro!')
# print(f'{" SAIDAS ":-^50}')
# if numero % 2 == 0:
#     print(f'O numero {numero} é par')
# else:
#     print(f'O numero {numero} é impar')

# SEGUNDO
# while ok:
#     try:
#         hora = int(input("Digite a hora atual em formato militar (0 a 24): "))
#         if hora < 0 or hora > 24:
#             print("Valor de hora incorreto!")
#         else:
#             ok = False
#     except:
#         print('Não é um número inteiro!')
# print(f'{" SAIDAS ":-^50}')
# mensagem = ""
# if hora > 0 and hora <= 11:
#     mensagem = "Bom dia!"
# if hora => 12 and <=17:
#     mensagem = "Boa tarde!"
# if hora >= 18:
#     mensagem = "Boa noite!"
# print(mensagem)

# TERCEIRO
# nome = input("Digite o seu nome: ")
# mensagem = ""
# if len(nome) < 4:
#     mensagem = "Seu nome é curto"
# if len(nome) > 4 and len(nome) <= 6:
#     mensagem = "Seu nome é normal"
# if len(nome) > 6:
#     mensagem = "Seu nome é muito grande"
# print(f'{" SAIDAS ":-^50}')
# print(mensagem)