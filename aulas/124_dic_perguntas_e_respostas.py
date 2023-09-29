perguntas = [
    {
        'pergunta': 'Quantos dedos tem um gato?',
        'opcoes': ['10', '12', '14', '16', '18', '20'],
        'resposta': '18',
    },
    {
        'pergunta': 'Quantos dedos tem um cachorro?',
        'opcoes': ['10', '12', '14', '16', '18', '20'],
        'resposta': '18',
    },
    {
        'pergunta': 'Quantos dedos tem uma iguana?',
        'opcoes': ['10', '12', '14', '16', '18', '20'],
        'resposta': '20',
    },
]

acertos = 0
print(f'{" JOGO DE PERGUNTAS ":{"="}^{50}}')

# for i in range(len(perguntas)):
for i in range(len(perguntas)):
    print(f' questao 0{i+1} '.center(50, '-'))
    print(perguntas[i]['pergunta'])
    for j in range(len(perguntas[i]['opcoes'])):
        print(f"{j}) {perguntas[i]['opcoes'][j]}")
    while True:
        try:
            valor = int(input("Escolha uma opcao: "))
            if 0 <= valor <= 5:
                break
            else:
                print("O valor deve estar entre 0 e 5. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico entre 0 e 5.")
    valor = perguntas[i]['opcoes'][valor]
    if perguntas[i]['resposta'] == valor:
        acertos += 1
    
print(f' Jogo Encerrado '.center(50, '='))
print(f' Pontuação: {acertos} '.center(50, '-'))