valor_do_compra = float(input("Digite o valor do pedido:(R$) "))
cliente_fidelidade = input("O cliente é fidelidade? (S/N) ").upper()
frete = 25

if valor_do_compra > 200 or cliente_fidelidade == "S":
    valor_final = valor_do_compra
    mensagem = "Parabéns! Você ganhou frete grátis!"
    print(f'frete grátis. valor final: R$ {mensagem}')

else: 
    valor_final = valor_do_compra + frete
    print(f'incluido o frete de R$ {frete}')
    print(f"Valor final : R$ {valor_final:.2f}")
