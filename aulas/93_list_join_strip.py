frase = "          shiroi nooto ni tsuzutta youni motto sunao ni hakidashitai yo nani kara nogaretainda "

lista_palavras_cortada_sem_espacos = frase.split()
print(lista_palavras_cortada_sem_espacos)

# se colocar r ou l antes do strip corta o espaco da direita ou da esquerda, apenas
frase_sem_espaco_no_comeco_e_fim = frase.strip()
print(frase_sem_espaco_no_comeco_e_fim)

print(''.join(lista_palavras_cortada_sem_espacos))