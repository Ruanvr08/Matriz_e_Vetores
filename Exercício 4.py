'''Uma pequena loja de artesanato possui apenas um vendedor e comercializa 10 tipos de objetos
diferentes. O vendedor recebe um salário de R$1100,00 acrescido de 5% do valor total de suas
vendas. O valor unitário dos objetos deve ser informado e armazenado em um vetor; a quantidade
vendida de cada objeto deve ficar em outro vetor, mas na mesma posição. Crie um programa que
receba os preços e as quantidades vendidas, armazenando-os em seus respectivos vetores. Depois,
determine e mostre:

a) A quantidade vendida, valor unitário e valor total de cada objeto. Ao final, deverão ser mostrados
o valor total das vendas e o valor da comissão que será paga ao vendedor.

b) O valor do objeto mais vendido e sua posição no vetor (em caso de empates mostre todos
empatados).'''

print('CATÁLOGO:')

objetos = ['SSD', 'Fone', 'Processador', 'Placa de Vídeo',
           'Fonte', 'Gabinete', 'Cooler', 'Memória RAM',
           'Mouse', 'Teclado']

valores = [120, 50, 80, 319, 239, 159, 160, 122, 40, 99]

for objeto, valor in zip(objetos,valores):
    print(f'{objeto}: {valor}')

vendas = []
soma = []
for objeto in objetos:
    qtd = int(input(f'Qual a quantidade vendida de {objeto}: '))
    vendas.append(qtd)

for objeto, valor, venda in zip(objetos, valores, vendas):
    print(f'{objeto}: {valor} R$')
    print(f'Quantidade vendida: {venda}')
    tt = valor * venda
    soma.append(tt)
ss = int(sum(soma))

print('')
print(f'O total de todas as vendas é {ss}')
print(f'O vendedor recebeu {ss * 0.10} R$ de comissão ')

