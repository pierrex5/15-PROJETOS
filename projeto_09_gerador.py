import random
import time
import json
from datetime import datetime

class GeradorAleatorio:
    def __init__(self):
        self.historico = []
        self.carregar_historico()
    
    def carregar_historico(self):
        """Carrega o histórico de gerações do arquivo"""
        try:
            with open('historico_geracoes.json', 'r', encoding='utf-8') as f:
                self.historico = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.historico = []
    
    def salvar_historico(self):
        """Salva o histórico no arquivo"""
        with open('historico_geracoes.json', 'w', encoding='utf-8') as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=2)
    
    def gerar_numeros(self, quantidade, minimo, maximo, permitir_repetidos=True, ordenar=False):
        """
        Gera números aleatórios baseado nos parâmetros do usuário
        """
        numeros_gerados = []
        
        # Verificar se é possível gerar sem repetição
        if not permitir_repetidos and (maximo - minimo + 1) < quantidade:
            return None, f"❌ Impossível gerar {quantidade} números únicos no intervalo {minimo}-{maximo}"
        
        # Gerar números
        while len(numeros_gerados) < quantidade:
            numero = random.randint(minimo, maximo)
            
            if permitir_repetidos or numero not in numeros_gerados:
                numeros_gerados.append(numero)
        
        # Ordenar se solicitado
        if ordenar:
            numeros_gerados.sort()
        
        # Salvar no histórico
        geracao = {
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'quantidade': quantidade,
            'minimo': minimo,
            'maximo': maximo,
            'repetidos': permitir_repetidos,
            'ordenado': ordenar,
            'numeros': numeros_gerados
        }
        
        self.historico.append(geracao)
        self.salvar_historico()
        
        return numeros_gerados, "✅ Geração concluída com sucesso!"
    
    def validar_entrada_numerica(self, mensagem, tipo=int, minimo=None, maximo=None):
        """
        Valida entradas numéricas do usuário com laço while
        """
        while True:
            try:
                valor = tipo(input(mensagem))
                
                if minimo is not None and valor < minimo:
                    print(f"❌ O valor deve ser maior ou igual a {minimo}")
                    continue
                    
                if maximo is not None and valor > maximo:
                    print(f"❌ O valor deve ser menor ou igual a {maximo}")
                    continue
                
                return valor
                
            except ValueError:
                print("❌ Por favor, digite um número válido!")
    
    def mostrar_estatisticas(self, numeros):
        """
        Mostra estatísticas dos números gerados
        """
        if not numeros:
            return
        
        print("\n📊 ESTATÍSTICAS:")
        print(f"   • Quantidade: {len(numeros)} números")
        print(f"   • Mínimo: {min(numeros)}")
        print(f"   • Máximo: {max(numeros)}")
        print(f"   • Média: {sum(numeros) / len(numeros):.2f}")
        print(f"   • Soma: {sum(numeros)}")
        
        # Moda (valor mais frequente)
        frequencia = {}
        for num in numeros:
            frequencia[num] = frequencia.get(num, 0) + 1
        
        moda = max(frequencia, key=frequencia.get)
        print(f"   • Moda: {moda} (aparece {frequencia[moda]} vezes)")
        
        # Mediana
        sorted_nums = sorted(numeros)
        n = len(sorted_nums)
        if n % 2 == 0:
            mediana = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            mediana = sorted_nums[n//2]
        print(f"   • Mediana: {mediana}")
    
    def mostrar_historico(self):
        """
        Mostra o histórico de gerações
        """
        print("\n" + "="*60)
        print("📜 HISTÓRICO DE GERAÇÕES")
        print("="*60)
        
        if not self.historico:
            print("📭 Nenhuma geração registrada.")
            return
        
        # Mostrar últimas 5 gerações
        historico_recente = self.historico[-5:]
        
        for i, geracao in enumerate(reversed(historico_recente), 1):
            print(f"\n--- Geração {len(self.historico) - i + 1} ---")
            print(f"📅 Data: {geracao['data']}")
            print(f"🔢 {geracao['quantidade']} números de {geracao['minimo']} a {geracao['maximo']}")
            print(f"🔄 Repetidos: {'Sim' if geracao['repetidos'] else 'Não'}")
            print(f"📈 Ordenado: {'Sim' if geracao['ordenado'] else 'Não'}")
            print(f"🎯 Números: {', '.join(map(str, geracao['numeros'][:10]))}" + 
                  ("..." if len(geracao['numeros']) > 10 else ""))
    
    def limpar_historico(self):
        """
        Limpa o histórico de gerações
        """
        confirmacao = input("\n⚠️  Tem certeza que deseja limpar todo o histórico? (s/n): ").strip().lower()
        if confirmacao in ['s', 'sim']:
            self.historico = []
            self.salvar_historico()
            print("✅ Histórico limpo com sucesso!")
        else:
            print("❕ Operação cancelada.")
    
    def gerar_com_animacao(self, quantidade, minimo, maximo, permitir_repetidos, ordenar):
        """
        Gera números com animação visual
        """
        print(f"\n🎲 Gerando {quantidade} números entre {minimo} e {maximo}...")
        print("⏳ ", end="", flush=True)
        
        # Animação de loading
        for i in range(10):
            print("■", end="", flush=True)
            time.sleep(0.1)
        
        print(" ✅")
        
        # Gerar números
        numeros, mensagem = self.gerar_numeros(quantidade, minimo, maximo, permitir_repetidos, ordenar)
        
        return numeros, mensagem

def main():
    """
    Função principal do programa
    """
    gerador = GeradorAleatorio()
    
    print("🎰 GERADOR DE VALORES ALEATÓRIOS")
    print("=" * 40)
    
    while True:
        print("\n" + "="*50)
        print("🎯 MENU PRINCIPAL")
        print("="*50)
        print("1. 🎲 Gerar números aleatórios")
        print("2. 🎯 Gerador rápido (configurações comuns)")
        print("3. 📜 Ver histórico")
        print("4. 🗑️  Limpar histórico")
        print("5. 📊 Estatísticas gerais")
        print("6. 🚪 Sair")
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        if opcao == '1':
            print("\n" + "="*40)
            print("🎲 GERADOR PERSONALIZADO")
            print("="*40)
            
            # Quantidade
            quantidade = gerador.validar_entrada_numerica(
                "Quantidade de números a gerar: ", 
                minimo=1, 
                maximo=1000
            )
            
            # Intervalo
            minimo = gerador.validar_entrada_numerica("Valor mínimo: ")
            maximo = gerador.validar_entrada_numerica("Valor máximo: ", minimo=minimo+1)
            
            # Configurações adicionais
            permitir_repetidos = input("Permitir números repetidos? (s/n) [s]: ").strip().lower() != 'n'
            
            ordenar = input("Ordenar números? (s/n) [n]: ").strip().lower() == 's'
            
            # Gerar com animação
            numeros, mensagem = gerador.gerar_com_animacao(
                quantidade, minimo, maximo, permitir_repetidos, ordenar
            )
            
            if numeros:
                print(f"\n{mensagem}")
                print(f"\n🎯 NÚMEROS GERADOS ({len(numeros)}):")
                print("-" * 50)
                
                # Mostrar em colunas para melhor visualização
                for i in range(0, len(numeros), 10):
                    linha = numeros[i:i+10]
                    print("  ".join(f"{num:6d}" for num in linha))
                
                # Estatísticas
                gerador.mostrar_estatisticas(numeros)
            else:
                print(f"\n{mensagem}")
        
        elif opcao == '2':
            print("\n" + "="*40)
            print("🎯 GERADOR RÁPIDO")
            print("="*40)
            print("1. Dados (1-6)")
            print("2. Loteria (1-60, 6 números)")
            print("3. Moeda (Cara/Coroa)")
            print("4. Porcentagem (0-100)")
            print("5. Cartas (1-13)")
            
            escolha_rapida = input("\nEscolha um tipo (1-5): ").strip()
            
            if escolha_rapida == '1':
                # Dados
                quantidade_dados = gerador.validar_entrada_numerica("Quantidade de dados: ", minimo=1, maximo=10)
                numeros, _ = gerador.gerar_numeros(quantidade_dados, 1, 6, True, False)
                print(f"\n🎲 Resultado dos dados: {', '.join(map(str, numeros))}")
                
            elif escolha_rapida == '2':
                # Loteria
                numeros, _ = gerador.gerar_numeros(6, 1, 60, False, True)
                print(f"\n🏆 Números da loteria: {', '.join(map(str, numeros))}")
                
            elif escolha_rapida == '3':
                # Moeda
                resultado = random.choice(['Cara', 'Coroa'])
                print(f"\n🪙 Resultado: {resultado}")
                
            elif escolha_rapida == '4':
                # Porcentagem
                quantidade = gerador.validar_entrada_numerica("Quantidade de porcentagens: ", minimo=1, maximo=20)
                numeros, _ = gerador.gerar_numeros(quantidade, 0, 100, True, False)
                print(f"\n📊 Porcentagens: {', '.join(map(str, numeros))}%")
                
            elif escolha_rapida == '5':
                # Cartas
                numeros, _ = gerador.gerar_numeros(5, 1, 13, False, True)
                valores_cartas = {1: 'Ás', 11: 'Valete', 12: 'Dama', 13: 'Rei'}
                cartas = [valores_cartas.get(num, str(num)) for num in numeros]
                print(f"\n🃏 Cartas: {', '.join(cartas)}")
                
            else:
                print("❌ Opção inválida!")
        
        elif opcao == '3':
            gerador.mostrar_historico()
        
        elif opcao == '4':
            gerador.limpar_historico()
        
        elif opcao == '5':
            print("\n" + "="*40)
            print("📊 ESTATÍSTICAS GERAIS")
            print("="*40)
            print(f"📈 Total de gerações realizadas: {len(gerador.historico)}")
            
            if gerador.historico:
                total_numeros = sum(len(geracao['numeros']) for geracao in gerador.historico)
                print(f"🔢 Total de números gerados: {total_numeros}")
                
                # Última geração
                ultima = gerador.historico[-1]
                print(f"🕒 Última geração: {ultima['data']}")
        
        elif opcao == '6':
            print("\n" + "="*40)
            print("👋 SAINDO DO GERADOR")
            print("="*40)
            print(f"📊 Total de gerações nesta sessão: {len(gerador.historico)}")
            print("Obrigado por usar o Gerador Aleatório! 🎲")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")

def demonstrar_random():
    """
    Demonstra as funções do módulo random
    """
    print("\n" + "="*50)
    print("🔧 DEMONSTRAÇÃO DO MÓDULO RANDOM")
    print("="*50)
    
    print("\n1. random.randint(1, 10):")
    for _ in range(5):
        print(f"   Número: {random.randint(1, 10)}")
    
    print("\n2. random.choice(['maçã', 'banana', 'laranja']):")
    frutas = ['maçã', 'banana', 'laranja']
    for _ in range(3):
        print(f"   Fruta: {random.choice(frutas)}")
    
    print("\n3. random.uniform(1.5, 5.5):")
    for _ in range(3):
        print(f"   Decimal: {random.uniform(1.5, 5.5):.2f}")
    
    print("\n4. random.sample(range(1, 11), 3):")
    print(f"   Amostra única: {random.sample(range(1, 11), 3)}")
    
    print("\n5. Embaralhando lista:")
    lista = [1, 2, 3, 4, 5]
    print(f"   Original: {lista}")
    random.shuffle(lista)
    print(f"   Embaralhada: {lista}")

if __name__ == "__main__":
    # Mostrar demonstração das funções random
    demonstrar_random()
    
    input("\nPressione Enter para iniciar o gerador...")
    
    # Iniciar programa principal
    main()