estoque = {}

def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))
    
    estoque[codigo] = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    print("Produto cadastrado!\n")

def listar_produtos():
    print("\n--- ESTOQUE ---")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo} | Nome: {produto['nome']} | "
              f"Quantidade: {produto['quantidade']} | Preço: R$ {produto['preco']:.2f}")
    print()

def entrada_estoque():
    codigo = input("Código do produto: ")
    if codigo in estoque:
        quantidade = int(input("Quantidade a adicionar: "))
        estoque[codigo]['quantidade'] += quantidade
        print("Entrada registrada!\n")
    else:
        print("Produto não encontrado!\n")

def saida_estoque():
    codigo = input("Código do produto: ")
    if codigo in estoque:
        quantidade = int(input("Quantidade a retirar: "))
        if estoque[codigo]['quantidade'] >= quantidade:
            estoque[codigo]['quantidade'] -= quantidade
            print("Saída registrada!\n")
        else:
            print("Quantidade insuficiente em estoque!\n")
    else:
        print("Produto não encontrado!\n")

# Menu principal
while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada no estoque")
    print("4 - Saída do estoque")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        entrada_estoque()
    elif opcao == '4':
        saida_estoque()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")