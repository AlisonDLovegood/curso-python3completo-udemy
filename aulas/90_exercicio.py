lista_compras = []
print(f'='*50)
print(f'{" LISTA DE COMPRAS ":-^50}')

while True:
    ipt = input(f'{"[i]nserir [a]pagar [l]istar [s]air": ^50}\n')
    
    if ipt == 'i':
        lista_compras.append(input("Entre com o novo item da lista: "))
    elif ipt == 'a':
        try:
            lista_compras.pop(int(input("Digite o indice do item a remover: ")))
        except ValueError:
            print(f'Esse valor é inválido, por favor digite um número inteiro!')
        except IndexError:
            print(f'Esse indice nao existe na lista!')
    elif ipt == 'l':
        for i, item in enumerate(lista_compras):
            print(f'indice: {i}\titem: {item}')
    elif ipt == 's':
        print("Finalizado!")
        break
    else:
        print("Valor de entrada invalido, tecle uma das opcoes validas!")