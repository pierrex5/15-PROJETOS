def main():
    """
    Versão simplificada da lista de contatos
    """
    contatos = []
    
    print("📒 LISTA DE CONTATOS SIMPLES")
    print("=" * 30)
    
    while True:
        print("\nOpções:")
        print("1. Adicionar contato")
        print("2. Ver contatos") 
        print("3. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == '1':
            print("\n--- Adicionar Contato ---")
            
            # Laço para nome válido
            while True:
                nome = input("Nome: ").strip()
                if nome:
                    break
                print("❌ Nome é obrigatório!")
            
            # Laço para telefone válido  
            while True:
                telefone = input("Telefone: ").strip()
                if telefone:
                    break
                print("❌ Telefone é obrigatório!")
            
            contato = {'nome': nome, 'telefone': telefone}
            contatos.append(contato)
            print(f"✅ {nome} adicionado!")
        
        elif opcao == '2':
            print("\n--- Lista de Contatos ---")
            
            if not contatos:
                print("📭 Lista vazia")
            else:
                i = 0
                while i < len(contatos):
                    print(f"{i + 1}. {contatos[i]['nome']} - {contatos[i]['telefone']}")
                    i += 1
        
        elif opcao == '3':
            print(f"\n👋 Saindo... Total de contatos: {len(contatos)}")
            break
        
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()