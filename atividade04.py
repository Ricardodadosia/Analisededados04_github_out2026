from unittest import case


print('''Setores:
[1] - Sul 
[2] - Norte 
[3] - leste 
[4] - oeste 
[5] a [6] - Nordeste 
[7] a [9] - sudeste 
[10] - centro - oeste 
[11] - noroeste 
''')
opcao = int(input('informe o codigo de origem: '))

match opcao:
    case 1:
        print('sul')
    case 2:
        print('norte')
    case 3:
        print('leste')
    case 4:
        print('oeste')
    case opcao if 5 <= opcao <= 6:
        print('Nordeste')
    case opcao if 7 <= opcao <= 9:
        print('sudeste')
    case 10:
        print('centro - oeste')
    case 11:
        print('noroeste')
    case _:
        print('Importado') 