import random

print(f'='*50)
print(f'{" GERADOR DE CPF ":-^50}')

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

aux = 10
valores = []
for i in range(len(cpf)):
    valores.append(int(cpf[i])*aux)
    aux -= 1
resultado = (sum(valores) * 10) % 11
digito = resultado if resultado <= 9 else 0
cpf = cpf + str(digito)

aux = 11
valores.clear()
for i in range(len(cpf)):
    valores.append(int(cpf[i])*aux)
    aux -= 1
resultado = (sum(valores) * 10) % 11
digito = resultado if resultado <= 9 else 0
cpf = cpf + str(digito)

print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')