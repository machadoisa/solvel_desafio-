
codigo = int(input("Boa tarde, o que voce deseja comprar? 1 - Jogo de talheres (500$) / 2 - Lapis de cor (25$) /3 - Finalizar carrinho "))


if codigo == 1:
    print('Jogo de talheres. O pagamento deve ser feito com 5 notas de 100 reais')


elif codigo == 2:
    print('Lápis de cor. O pagamento deve ser feito com 2 notas de 10 reais e uma nota de 5 reais')

else:
    print('carrinho finalizado')


print('Obg pela compra')