def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    Fórmula: IMC = peso / (altura × altura)
    """
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a OMS (Organização Mundial da Saúde)
    """
    if imc < 18.5:
        return "Abaixo do peso", "⚠️"
    elif 18.5 <= imc < 25:
        return "Peso normal", "✅"
    elif 25 <= imc < 30:
        return "Sobrepeso", "⚠️"
    elif 30 <= imc < 35:
        return "Obesidade Grau I", "🔶"
    elif 35 <= imc < 40:
        return "Obesidade Grau II", "🔴"
    else:
        return "Obesidade Grau III", "💀"

def mostrar_tabela_imc():
    """
    Exibe a tabela de classificação do IMC
    """
    print("\n" + "="*50)
    print("📊 TABELA DE CLASSIFICAÇÃO DO IMC")
    print("="*50)
    print("IMC          | Classificação")
    print("-" * 50)
    print("Abaixo de 18,5 | Abaixo do peso")
    print("18,5 - 24,9    | Peso normal")
    print("25,0 - 29,9    | Sobrepeso")
    print("30,0 - 34,9    | Obesidade Grau I")
    print("35,0 - 39,9    | Obesidade Grau II")
    print("Acima de 40,0  | Obesidade Grau III")
    print("="*50)

def validar_entrada_numero(mensagem):
    """
    Valida se a entrada é um número positivo
    """
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor <= 0:
                print("❌ O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("❌ Por favor, digite um número válido.")

def calcular_imc_multiplas_pessoas():
    """
    Calcula o IMC para múltiplas pessoas
    """
    pessoas = []
    
    print("\n" + "="*50)
    print("👥 CÁLCULO DE IMC PARA MÚLTIPLAS PESSOAS")
    print("="*50)
    
    while True:
        print(f"\nPessoa {len(pessoas) + 1}:")
        nome = input("Nome (ou 'sair' para finalizar): ").strip()
        
        if nome.lower() == 'sair':
            break
            
        peso = validar_entrada_numero("Peso (kg): ")
        altura = validar_entrada_numero("Altura (m): ")
        
        imc = calcular_imc(peso, altura)
        classificacao, emoji = classificar_imc(imc)
        
        pessoa = {
            'nome': nome,
            'peso': peso,
            'altura': altura,
            'imc': imc,
            'classificacao': classificacao,
            'emoji': emoji
        }
        
        pessoas.append(pessoa)
        print(f"✅ {nome} - IMC: {imc:.1f} - {classificacao} {emoji}")
    
    return pessoas

def exibir_relatorio(pessoas):
    """
    Exibe um relatório completo com todos os cálculos
    """
    if not pessoas:
        print("\n❌ Nenhum dado para exibir.")
        return
    
    print("\n" + "="*60)
    print("📈 RELATÓRIO COMPLETO DE IMC")
    print("="*60)
    
    for pessoa in pessoas:
        print(f"\n👤 Nome: {pessoa['nome']}")
        print(f"⚖️  Peso: {pessoa['peso']:.1f} kg")
        print(f"📏 Altura: {pessoa['altura']:.2f} m")
        print(f"🧮 IMC: {pessoa['imc']:.1f}")
        print(f"📊 Classificação: {pessoa['classificacao']} {pessoa['emoji']}")
        print("-" * 40)

def calcular_peso_ideal(altura):
    """
    Calcula a faixa de peso ideal baseada no IMC
    """
    peso_minimo = 18.5 * (altura ** 2)
    peso_maximo = 24.9 * (altura ** 2)
    return peso_minimo, peso_maximo

def mostrar_recomendacoes(imc, classificacao):
    """
    Mostra recomendações baseadas na classificação do IMC
    """
    print("\n" + "="*50)
    print("💡 RECOMENDAÇÕES")
    print("="*50)
    
    if classificacao == "Abaixo do peso":
        print("""
        🔸 Consulte um nutricionista para ganho de peso saudável
        🔸 Aumente o consumo de alimentos nutritivos
        🔸 Pratique exercícios de força
        🔸 Mantenha uma rotina alimentar regular
        """)
    elif classificacao == "Peso normal":
        print("""
        ✅ Parabéns! Mantenha seus hábitos saudáveis
        ✅ Continue com alimentação balanceada
        ✅ Pratique atividades físicas regularmente
        ✅ Faça check-ups anuais
        """)
    elif classificacao == "Sobrepeso":
        print("""
        🔸 Considere reduzir o consumo de calorias
        🔸 Aumente a prática de atividades físicas
        🔸 Prefira alimentos integrais e naturais
        🔸 Beba bastante água
        """)
    else:  # Obesidade
        print("""
        🔴 Procure orientação médica e nutricional
        🔴 Estabeleça metas realistas de perda de peso
        🔴 Adote uma alimentação balanceada
        🔴 Pratique exercícios regularmente
        🔴 Considere acompanhamento psicológico se necessário
        """)

def main():
    """
    Função principal do programa
    """
    print("🎯 PROGRAMA DE CÁLCULO DE IMC")
    print("=" * 40)
    
    while True:
        print("\n" + "="*50)
        print("📋 MENU PRINCIPAL")
        print("="*50)
        print("1. Calcular IMC individual")
        print("2. Calcular IMC para múltiplas pessoas")
        print("3. Ver tabela de classificação")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            print("\n" + "="*40)
            print("👤 CÁLCULO DE IMC INDIVIDUAL")
            print("="*40)
            
            peso = validar_entrada_numero("Digite seu peso (kg): ")
            altura = validar_entrada_numero("Digite sua altura (m): ")
            
            imc = calcular_imc(peso, altura)
            classificacao, emoji = classificar_imc(imc)
            
            print(f"\n📊 RESULTADO:")
            print(f"• Peso: {peso:.1f} kg")
            print(f"• Altura: {altura:.2f} m")
            print(f"• IMC: {imc:.1f}")
            print(f"• Classificação: {classificacao} {emoji}")
            
            # Mostrar peso ideal
            peso_min, peso_max = calcular_peso_ideal(altura)
            print(f"• Faixa de peso ideal: {peso_min:.1f} kg a {peso_max:.1f} kg")
            
            # Mostrar recomendações
            mostrar_recomendacoes(imc, classificacao)
            
        elif opcao == '2':
            pessoas = calcular_imc_multiplas_pessoas()
            if pessoas:
                exibir_relatorio(pessoas)
                
                # Estatísticas
                total_pessoas = len(pessoas)
                imcs = [p['imc'] for p in pessoas]
                imc_medio = sum(imcs) / total_pessoas
                
                print(f"\n📈 ESTATÍSTICAS:")
                print(f"• Total de pessoas: {total_pessoas}")
                print(f"• IMC médio do grupo: {imc_medio:.1f}")
                
        elif opcao == '3':
            mostrar_tabela_imc()
            
        elif opcao == '4':
            print("\n👋 Obrigado por usar o programa de cálculo de IMC!")
            print("Cuide da sua saúde! 💚")
            break
            
        else:
            print("❌ Opção inválida! Por favor, escolha entre 1 e 4.")

# Informações sobre o IMC
def sobre_imc():
    """
    Informações importantes sobre o IMC
    """
    print("\n" + "="*50)
    print("ℹ️  INFORMAÇÕES SOBRE O IMC")
    print("="*50)
    print("""
    O Índice de Massa Corporal (IMC) é uma medida internacional
    usada para calcular se uma pessoa está no peso ideal.
    
    📝 LIMITAÇÕES:
    • Não considera a composição corporal (músculo vs gordura)
    • Não é adequado para atletas e idosos
    • Não considera distribuição de gordura
    
    💡 RECOMENDAÇÃO:
    Consulte sempre um profissional de saúde para uma
    avaliação completa da sua saúde.
    """)

if __name__ == "__main__":
    # Mostrar informações sobre IMC no início
    sobre_imc()
    input("\nPressione Enter para continuar...")
    main()
    