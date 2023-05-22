"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# modulo do python de expressao regular 
import re
import sys

print(f'='*50)
print(f'{" Calculo do segundo dígito do CPF ":-^50}')
ipt = input('Digite o numero do CPF do cidadao: ')

# verificar se são caracteres repetidos, ex: caso em que se entra com 111.111.111-11
entrada_valor_repetido = ipt == ipt[0] * len(ipt)
if entrada_valor_repetido:
    print('Valor de entrada inválido!')
    sys.exit()

# metodo sub de substituição
cpf = re.sub(
    r'[^0-9]', # r de expressao regular, verifica tudo que não é um número nesse caso 
    '', # substitui para nada, apenas "apaga"
    ipt
    )

# PARA O PRIMEIRO
cpf_cortado = cpf[:9]
aux = 10
valores = []
for i in range(len(cpf_cortado)):
    valores.append(int(cpf_cortado[i])*aux)
    aux -= 1
resultado = (sum(valores) * 10) % 11
digito = resultado if resultado <= 9 else 0
cpf_cortado = cpf_cortado + str(digito)

# PARA O SEGUNDO
aux = 11
valores.clear()
for i in range(len(cpf_cortado)):
    valores.append(int(cpf_cortado[i])*aux)
    aux -= 1
resultado = (sum(valores) * 10) % 11
digito = resultado if resultado <= 9 else 0
cpf_cortado = cpf_cortado + str(digito)

if cpf == cpf_cortado:
    print(f'O NÚMERO DE CPF É VÁLIDO')
else:
    print(f'O NÚMERO DE CPF É INVÁLIDO')
