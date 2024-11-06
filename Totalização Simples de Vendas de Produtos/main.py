_ = '='*41
print(_)
print('Totalização Simples de Vendas de Produtos')
print(_)

arquivo = open('vendas.csv', 'r')
vendas = []
for i, linha in enumerate(arquivo.readlines()):
    vendas.append(linha.split(';'))
    vendas[i][0] = int(vendas[i][0])
    vendas[i][1] = int(vendas[i][1])
    vendas[i][2] = float(vendas[i][2].replace(',', '.'))
arquivo.close()

codigo = int(input('Digite o código: '))
while codigo != 0:
    while codigo < 10000 or codigo > 21000:
        print(f'{codigo} Código inválido (deve ser entre 10000 e 21000)\n')
        codigo = int(input('Digite o código: '))

    total = 0
    for i in range(len(vendas)):
        if codigo == vendas[i][0]:
            total += vendas[i][1] * vendas[i][2]
    print(f'Total vendido do produto {codigo} = R$ {total:.2f}\n')

    codigo = int(input('Digite o código: '))

print('\nFim do programa')
print(_)
