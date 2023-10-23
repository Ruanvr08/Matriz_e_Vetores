# Escrever um programa que lê um vetor N de tamanho 20 e o imprime na tela. Em seguida, troque
# o 1º elemento com o último, o 2ª com o penúltimo, ... até o 10ª com o 11º. Imprima o vetor N
# modificado

import random

vet1 = []

for a in range(0,20):
    rand = random.randint(0, 100)
    vet1.append(rand)

vetMod = vet1[::-1]

print(f'Vetor: {vet1}')
print('-=' * 80)
print(f'Vetor Modificado: {vetMod}')