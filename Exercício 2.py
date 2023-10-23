#Faça um programa que some o conteúdo de dois vetores de tamanho 25 e armazene o resultado
# em um terceiro vetor. Imprima os três vetores na tela

import random

vet1 = []
vet2 = []
vet3 = []

for a in range(0,25):
    rand = random.randint(0, 100)
    vet1.append(rand)

for a in range(0,25):
    randr = random.randint(0, 100)
    vet2.append(randr)

for n1, n2 in zip(vet1, vet2):
    sm = n1 + n2
    vet3.append(sm)
print(f'Vetor 1 {vet1}')
print('-=' * 80)
print(f'Vetor 2 {vet2}')
print('-=' * 80)
print(f'Vetor 3: {vet3}')