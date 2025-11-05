import os
import datetime
import random
import json

# ==================== FUNÇÕES DA CALCULADORA ====================
def calculadora():
    """Calculadora com operações básicas"""
    while True:
        print("\n" + "="*40)
        print("🧮 CALCULADORA")
        print("="*40)
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma operação (1-5): ")
        
        if opcao == '5':
            break
            
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == '1':
                    resultado = num1 + num2
                    print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")
                elif opcao == '2':
                    resultado = num1 - num2
                    print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")
                elif opcao == '3':
                    resultado = num1 * num2
                    print(f"\n✅ Resultado: {num1} × {num2} = {resultado}")
                elif opcao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"\n✅ Resultado: {num1} ÷ {num2} = {resultado}")
                    else:
                        print("\n❌ Erro: Não é possível dividir por zero!")
            except ValueError:
                print("\n❌ Erro: Digite números válidos!")
        else:
            print("\n❌ Opção inválida!")

# ==================== FUNÇÕES DA AGENDA ====================
AGENDA_FILE = "agenda.json"

def carregar_agenda():
    """Carrega a agenda do arquivo JSON"""
    try:
        with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_agenda(agenda):
    """Salva a agenda no arquivo JSON"""
    with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=2)

def adicionar_contato():
    """Adiciona um novo contato à agenda"""
    print("\n" + "="*40)
    print("📒 ADICIONAR CONTATO")
    print("="*40)
    
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    if nome:
        agenda = carregar_agenda()
        novo_contato = {
            "id": len(agenda) + 1,
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "data_cadastro": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        agenda.append(novo_contato)
        salvar_agenda(agenda)
        print(f"\n✅ Contato '{nome}' adicionado com sucesso!")
    else:
        print("\n❌ Nome é obrigatório!")

def listar_contatos():
    """Lista todos os contatos da agenda"""
    agenda = carregar_agenda()
    
    print("\n" + "="*50)
    print("📋 LISTA DE CONTATOS")
    print("="*50)
    
    if not agenda:
        print("Nenhum contato cadastrado.")
        return
    
    for contato in agenda:
        print(f"ID: {contato['id']}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        print(f"Cadastro: {contato['data_cadastro']}")
        print("-" * 30)

def buscar_contato():
    """Busca contatos por nome"""
    termo = input("\n🔍 Digite o nome para buscar: ").strip().lower()
    agenda = carregar_agenda()
    encontrados = []
    
    for contato in agenda:
        if termo in contato['nome'].lower():
            encontrados.append(contato)
    
    if encontrados:
        print(f"\n📄 Encontrados {len(encontrados)} contato(s):")
        for contato in encontrados:
            print(f"- {contato['nome']} | {contato['telefone']} | {contato['email']}")
    else:
        print("\n❌ Nenhum contato encontrado.")

def agenda_contatos():
    """Menu principal da agenda"""
    while True:
        print("\n" + "="*40)
        print("📒 AGENDA DE CONTATOS")
        print("="*40)
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            break
        else:
            print("\n❌ Opção inválida!")

# ==================== GERADOR DE RELATÓRIOS ====================
def gerar_relatorio_contatos():
    """Gera um relatório dos contatos"""
    agenda = carregar_agenda()
    
    print("\n" + "="*50)
    print("📊 RELATÓRIO DE CONTATOS")
    print("="*50)
    
    if not agenda:
        print("Nenhum contato para gerar relatório.")
        return
    
    total_contatos = len(agenda)
    data_geracao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"Data de geração: {data_geracao}")
    print(f"Total de contatos: {total_contatos}")
    print("\n📋 Lista completa:")
    print("-" * 50)
    
    for contato in agenda:
        print(f"• {contato['nome']} - {contato['telefone']} - {contato['email']}")
    
    # Salvar relatório em arquivo
    with open("relatorio_contatos.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE CONTATOS\n")
        f.write("=" * 30 + "\n")
        f.write(f"Data: {data_geracao}\n")
        f.write(f"Total de contatos: {total_contatos}\n\n")
        for contato in agenda:
            f.write(f"- {contato['nome']} | {contato['telefone']} | {contato['email']}\n")
    
    print(f"\n💾 Relatório salvo em 'relatorio_contatos.txt'")

def gerar_relatorio_sistema():
    """Gera um relatório do sistema"""
    data_atual = datetime.datetime.now()
    
    print("\n" + "="*50)
    print("📊 RELATÓRIO DO SISTEMA")
    print("="*50)
    
    print(f"Data e hora: {data_atual.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Dia da semana: {data_atual.strftime('%A')}")
    print(f"Ano: {data_atual.year}")
    print(f"Mês: {data_atual.month} ({data_atual.strftime('%B')})")
    
    # Verificar se arquivo de agenda existe
    if os.path.exists(AGENDA_FILE):
        agenda = carregar_agenda()
        print(f"Contatos na agenda: {len(agenda)}")
    else:
        print("Agenda: Não criada")

def gerador_relatorios():
    """Menu do gerador de relatórios"""
    while True:
        print("\n" + "="*40)
        print("📊 GERADOR DE RELATÓRIOS")
        print("="*40)
        print("1. Relatório de contatos")
        print("2. Relatório do sistema")
        print("3. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == '1':
            gerar_relatorio_contatos()
        elif opcao == '2':
            gerar_relatorio_sistema()
        elif opcao == '3':
            break
        else:
            print("\n❌ Opção inválida!")

# ==================== FUNÇÕES EXTRAS ====================
def jogo_adivinhacao():
    """Jogo de adivinhação de números"""
    print("\n" + "="*40)
    print("🎮 JOGO DE ADIVINHAÇÃO")
    print("="*40)
    
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    max_tentativas = 5
    
    print(f"Tente adivinhar o número entre 1 e 50!")
    print(f"Você tem {max_tentativas} tentativas.")
    
    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"\n🎯 Tentativa {tentativas + 1}: "))
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
                return
            elif palpite < numero_secreto:
                print("📈 Tente um número MAIOR!")
            else:
                print("📉 Tente um número MENOR!")
                
            print(f"Tentativas restantes: {max_tentativas - tentativas}")
            
        except ValueError:
            print("❌ Digite um número válido!")
    
    print(f"\n💀 Fim de jogo! O número era {numero_secreto}")

def conversor_temperatura():
    """Conversor de temperatura"""
    print("\n" + "="*40)
    print("🌡️ CONVERSOR DE TEMPERATURA")
    print("="*40)
    
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        
        print(f"\n📊 RESULTADOS:")
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
        print(f"{celsius}°C = {kelvin:.2f}K")
    except ValueError:
        print("❌ Digite um número válido!")

# ==================== MENU PRINCIPAL ====================
def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("🚀 SISTEMA MULTIFUNCIONAL")
        print("="*50)
        print("1. 🧮 Calculadora")
        print("2. 📒 Agenda de Contatos")
        print("3. 📊 Gerador de Relatórios")
        print("4. 🎮 Jogo de Adivinhação")
        print("5. 🌡️ Conversor de Temperatura")
        print("6. ❌ Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ")
        
        if opcao == '1':
            calculadora()
        elif opcao == '2':
            agenda_contatos()
        elif opcao == '3':
            gerador_relatorios()
        elif opcao == '4':
            jogo_adivinhacao()
        elif opcao == '5':
            conversor_temperatura()
        elif opcao == '6':
            print("\n👋 Obrigado por usar o Sistema Multifuncional!")
            print("Até logo! 🚀")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

# ==================== INICIALIZAÇÃO ====================
if __name__ == "__main__":
    print("Bem-vindo ao Sistema Multifuncional! 🎉")
    menu_principal()