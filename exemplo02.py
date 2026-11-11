# Estrutura Match Case 

print('''
[1] - Marketing
[2] - financeiro 
[3] a [5]  Administração
[6] a [9] - TI
[10] a [20] - Serviços Gerais 
''')

opcao = int(input('Digite o número do setor: '))

match opcao:
    case 1:
        print('Você escolheu o setor de Marketing')
    case 2:
        print('Você escolheu o setor Financeiro')
    case 3 | 4 | 5:
        print('Você escolheu o setor de Administração')

    case opcao if 6 <= opcao <= 9:
        print('Você escolheu o setor de TI')

    case opcao if 10 <= opcao <= 20:
        print('Você escolheu o setor de Serviços Gerais')


    case _:
        print('Setor inválido')