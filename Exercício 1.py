vet1 = []
vet2 = []

for c in range(0,10):
    valor = int(input('Digite um número: '))
    vet1.append(valor)
for valor in vet1:
    quadrado = valor ** 2
    vet2.append(quadrado)


print(f'Vetor 1: {vet1}')
print(f'Vetor 2: {vet2}')

