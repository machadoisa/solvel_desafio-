print('Bem vindo ao carrinho de compras')

realizar_compras = int(input('Deseja realizar alguma compra? 1 - sim / 2 - Não '))
if realizar_compras == 1:
   print("Iniciando compra")

   opcao_produto = "1"
   produtos = []
   valor_produto = []
   resultado = 0

   while opcao_produto != "2":
       produtos.append(input("Informe o produto: "))
       valor_produto.append(int(input('Informe o valor do seu produto: ')))
       opcao_produto = input("Deseja continuar comprando? digite 1 - sim / 2 - Desejo ver minha lista de produtos: ")


for index in range(0, len(produtos), 1):
       produto_listado = produtos[index]
       valor_listado = valor_produto[index]
       print(f'O produto é {produto_listado} e seu valor é {valor_listado}')

for index in range(0, len(valor_produto), 1):
    resultado = resultado + valor_produto[index]

print(f'O total da compra é: {resultado}')












