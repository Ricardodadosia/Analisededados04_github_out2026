# um aplicativo de lanches da frete gratis se o pedido for maior de R$ 50,00 e a distancia for menor ou igual a 3 km.

valor_pedido = float(input("Digite o valor do pedido: "))
distancia = float(input("Digite a distância em km: "))
frete = 8

if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    print("Parabéns! Você ganhou frete grátis!")

else:
    valor_final = valor_pedido + frete
    print(f'frete de R$ {frete}')
    print(f"Valor final do pedido: R$ {valor_final:.2f}")


