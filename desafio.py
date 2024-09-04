


carrinho=[]
higiene=["Sabonete"]
alimento=["Picanha"]
produtos=["Gelo"]

login = int(input("Para logar digite\n 1- cliente\n 2- funcionário\n "))

if login == 1:
    login1= int(input("Digite seu cpf: "))

    while True:
        print("1- lista de produtos")
        print("2- visualizar o carrinho")
        print("3- Remover produto")
        print("4- Adicionar produto")
        print("5- Finalizar compra")
        op = int(input("Selecione a opção: "))

        if op == 1:
            print(f"A lista de Produtos é\nhigiene {higiene}\nalimento{alimento}\nprodutos{produtos}")
        
        if op == 2:
            print(f"os produtos do seu carrinho são:\n{carrinho}")
        
        if op == 4:
            p = int(input("Selecione O Produto:\n1-Picanha\n2-Sabonete\n3-Gelo\n"))

            if p == 1:
                carrinho.append("Picanha")
                print("Produto Adicionado")

            elif p == 2:
                carrinho.append("Sabonete")
                print("Produto Adicionado")
            
            elif p == 3:
                carrinho.append("Gelo")
                print("Produto Adicionado")
