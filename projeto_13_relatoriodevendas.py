# Projeto 13 — Relatório de Vendas

vendas = {}  # Dicionário para armazenar produtos, quantidades e preços

while True:
    print("\n===== SISTEMA DE RELATÓRIO DE VENDAS =====")
    print("1 - Registrar venda")
    print("2 - Mostrar relatório de vendas")
    print("3 - Listar produtos vendidos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # --- Registrar venda ---
    if opcao == "1":
        produto = input("Nome do produto: ").strip().title()
        try:
            quantidade = int(input("Quantidade vendida: "))
            preco = float(input("Preço unitário (R$): "))

            if produto in vendas:
                vendas[produto]["quantidade"] += quantidade
                vendas[produto]["total"] += quantidade * preco
            else:
                vendas[produto] = {
                    "quantidade": quantidade,
                    "preco": preco,
                    "total": quantidade * preco
                }

            print(f"✅ Venda de {quantidade}x '{produto}' registrada com sucesso!")
        except ValueError:
            print("⚠️ Digite valores numéricos válidos para quantidade e preço.")

    # --- Mostrar relatório ---
    elif opcao == "2":
        if len(vendas) == 0:
            print("📦 Nenhuma venda registrada.")
        else:
            total_geral = 0
            total_itens = 0
            mais_vendido = None
            maior_qtd = 0

            for produto, dados in vendas.items():
                total_geral += dados["total"]
                total_itens += dados["quantidade"]

                if dados["quantidade"] > maior_qtd:
                    maior_qtd = dados["quantidade"]
                    mais_vendido = produto

            media_faturamento = total_geral / len(vendas)

            print("\n===== RELATÓRIO DE VENDAS =====")
            print(f"💵 Total vendido (R$): {total_geral:.2f}")
            print(f"📦 Total de itens vendidos: {total_itens}")
            print(f"🏆 Produto mais vendido: {mais_vendido} ({maior_qtd} unidades)")
            print(f"📊 Média de faturamento por produto: R$ {media_faturamento:.2f}")

    # --- Listar produtos vendidos ---
    elif opcao == "3":
        if len(vendas) == 0:
            print("📦 Nenhum produto vendido ainda.")
        else:
            print("\n📋 PRODUTOS VENDIDOS:")
            print("-" * 45)
            for produto, dados in vendas.items():
                print(f"Produto: {produto}")
                print(f"Quantidade: {dados['quantidade']}")
                print(f"Preço Unitário: R$ {dados['preco']:.2f}")
                print(f"Total Vendido: R$ {dados['total']:.2f}")
                print("-" * 45)

    # --- Sair do sistema ---
    elif opcao == "4":
        print("👋 Encerrando o sistema de vendas. Até logo!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")