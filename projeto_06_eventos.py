import json
import os
from datetime import datetime
import re

class SistemaEvento:
    def __init__(self, arquivo_dados="participantes.json"):
        self.arquivo_dados = arquivo_dados
        self.participantes = self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega os participantes do arquivo JSON"""
        try:
            if os.path.exists(self.arquivo_dados):
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def salvar_dados(self):
        """Salva os participantes no arquivo JSON"""
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.participantes, f, ensure_ascii=False, indent=2)
    
    def validar_email(self, email):
        """Valida o formato do e-mail"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
    
    def validar_cpf(self, cpf):
        """Valida o formato do CPF (apenas formato, não cálculo de dígitos)"""
        # Remove caracteres não numéricos
        cpf_limpo = re.sub(r'[^0-9]', '', cpf)
        
        # Verifica se tem 11 dígitos
        if len(cpf_limpo) != 11:
            return False
        
        # Verifica se não é uma sequência repetida
        if cpf_limpo == cpf_limpo[0] * 11:
            return False
        
        return cpf_limpo
    
    def formatar_cpf(self, cpf):
        """Formata o CPF para o padrão XXX.XXX.XXX-XX"""
        cpf_limpo = self.validar_cpf(cpf)
        if cpf_limpo:
            return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
        return cpf
    
    def cpf_existe(self, cpf):
        """Verifica se o CPF já está cadastrado"""
        cpf_limpo = self.validar_cpf(cpf)
        if not cpf_limpo:
            return False
        
        for participante in self.participantes:
            if self.validar_cpf(participante['cpf']) == cpf_limpo:
                return True
        return False
    
    def cadastrar_participante(self):
        """Cadastra um novo participante"""
        print("\n" + "="*50)
        print("🎫 CADASTRO DE PARTICIPANTE")
        print("="*50)
        
        # Nome
        while True:
            nome = input("Nome completo: ").strip()
            if nome:
                if len(nome) >= 3:
                    break
                else:
                    print("❌ O nome deve ter pelo menos 3 caracteres.")
            else:
                print("❌ O nome é obrigatório.")
        
        # E-mail
        while True:
            email = input("E-mail: ").strip().lower()
            if email:
                if self.validar_email(email):
                    break
                else:
                    print("❌ E-mail inválido. Digite um e-mail válido.")
            else:
                print("❌ O e-mail é obrigatório.")
        
        # CPF
        while True:
            cpf = input("CPF: ").strip()
            cpf_validado = self.validar_cpf(cpf)
            if cpf_validado:
                if not self.cpf_existe(cpf):
                    cpf_formatado = self.formatar_cpf(cpf)
                    break
                else:
                    print("❌ Este CPF já está cadastrado.")
            else:
                print("❌ CPF inválido. Digite um CPF válido (11 dígitos).")
        
        # Gerar ID único
        if self.participantes:
            novo_id = max(p['id'] for p in self.participantes) + 1
        else:
            novo_id = 1
        
        # Criar participante
        participante = {
            'id': novo_id,
            'nome': nome,
            'email': email,
            'cpf': cpf_formatado,
            'data_cadastro': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'presente': False
        }
        
        self.participantes.append(participante)
        self.salvar_dados()
        
        print(f"\n✅ Participante cadastrado com sucesso!")
        print(f"📋 ID: {novo_id} | Nome: {nome}")
        return participante
    
    def listar_participantes(self):
        """Lista todos os participantes"""
        print("\n" + "="*60)
        print("📋 LISTA DE PARTICIPANTES")
        print("="*60)
        
        if not self.participantes:
            print("Nenhum participante cadastrado.")
            return
        
        print(f"Total de participantes: {len(self.participantes)}")
        print("-" * 60)
        
        for i, participante in enumerate(self.participantes, 1):
            status = "✅ Presente" if participante['presente'] else "❌ Ausente"
            print(f"{i:2d}. ID: {participante['id']:3d} | {participante['nome']:30} | {participante['email']:20} | {status}")
    
    def buscar_participante(self):
        """Busca participantes por nome, e-mail ou CPF"""
        print("\n" + "="*50)
        print("🔍 BUSCAR PARTICIPANTE")
        print("="*50)
        
        termo = input("Digite nome, e-mail ou CPF para buscar: ").strip().lower()
        
        if not termo:
            print("❌ Digite um termo para busca.")
            return
        
        encontrados = []
        for participante in self.participantes:
            if (termo in participante['nome'].lower() or 
                termo in participante['email'].lower() or 
                termo in participante['cpf'].replace('.', '').replace('-', '')):
                encontrados.append(participante)
        
        if encontrados:
            print(f"\n📄 Encontrados {len(encontrados)} participante(s):")
            print("-" * 50)
            for participante in encontrados:
                status = "✅ Presente" if participante['presente'] else "❌ Ausente"
                print(f"ID: {participante['id']} | {participante['nome']} | {participante['email']} | {participante['cpf']} | {status}")
        else:
            print("❌ Nenhum participante encontrado.")
    
    def marcar_presenca(self):
        """Marca presença de um participante"""
        print("\n" + "="*50)
        print("✅ MARCAR PRESENÇA")
        print("="*50)
        
        if not self.participantes:
            print("❌ Nenhum participante cadastrado.")
            return
        
        self.listar_participantes()
        
        try:
            id_participante = int(input("\nDigite o ID do participante para marcar presença: "))
            
            for participante in self.participantes:
                if participante['id'] == id_participante:
                    if not participante['presente']:
                        participante['presente'] = True
                        participante['hora_presenca'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        self.salvar_dados()
                        print(f"✅ Presença confirmada para {participante['nome']}!")
                    else:
                        print(f"ℹ️  {participante['nome']} já está marcado como presente.")
                    return
            
            print("❌ ID não encontrado.")
            
        except ValueError:
            print("❌ Digite um ID válido.")
    
    def gerar_relatorio(self):
        """Gera um relatório completo do evento"""
        print("\n" + "="*60)
        print("📊 RELATÓRIO DO EVENTO")
        print("="*60)
        
        total_participantes = len(self.participantes)
        presentes = sum(1 for p in self.participantes if p['presente'])
        ausentes = total_participantes - presentes
        
        print(f"📈 ESTATÍSTICAS:")
        print(f"   • Total de inscritos: {total_participantes}")
        print(f"   • Presentes: {presentes}")
        print(f"   • Ausentes: {ausentes}")
        
        if total_participantes > 0:
            percentual_presenca = (presentes / total_participantes) * 100
            print(f"   • Taxa de presença: {percentual_presenca:.1f}%")
        
        print(f"\n📋 LISTA DE PRESENTES:")
        if presentes > 0:
            for participante in self.participantes:
                if participante['presente']:
                    print(f"   ✅ {participante['nome']} - {participante['hora_presenca']}")
        else:
            print("   Nenhum participante presente ainda.")
        
        # Salvar relatório em arquivo
        self.salvar_relatorio_arquivo(presentes, ausentes, percentual_presenca)
    
    def salvar_relatorio_arquivo(self, presentes, ausentes, percentual):
        """Salva o relatório em um arquivo de texto"""
        nome_arquivo = f"relatorio_evento_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DO EVENTO\n")
            f.write("=" * 50 + "\n")
            f.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            
            f.write("ESTATÍSTICAS:\n")
            f.write(f"- Total de inscritos: {len(self.participantes)}\n")
            f.write(f"- Presentes: {presentes}\n")
            f.write(f"- Ausentes: {ausentes}\n")
            f.write(f"- Taxa de presença: {percentual:.1f}%\n\n")
            
            f.write("LISTA DE PARTICIPANTES:\n")
            f.write("-" * 50 + "\n")
            for participante in self.participantes:
                status = "PRESENTE" if participante['presente'] else "AUSENTE"
                f.write(f"{participante['id']:3d} | {participante['nome']:30} | {participante['email']:25} | {participante['cpf']:14} | {status}\n")
        
        print(f"\n💾 Relatório salvo em: {nome_arquivo}")
    
    def exportar_para_csv(self):
        """Exporta os dados para CSV"""
        import csv
        
        nome_arquivo = f"participantes_evento_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Nome', 'E-mail', 'CPF', 'Data Cadastro', 'Presente', 'Hora Presença'])
            
            for participante in self.participantes:
                writer.writerow([
                    participante['id'],
                    participante['nome'],
                    participante['email'],
                    participante['cpf'],
                    participante['data_cadastro'],
                    'Sim' if participante['presente'] else 'Não',
                    participante.get('hora_presenca', '')
                ])
        
        print(f"📤 Dados exportados para: {nome_arquivo}")
    
    def menu_principal(self):
        """Menu principal do sistema"""
        while True:
            print("\n" + "="*50)
            print("🎪 SISTEMA DE REGISTRO DE EVENTO")
            print("="*50)
            print("1. 🎫 Cadastrar participante")
            print("2. 📋 Listar participantes")
            print("3. 🔍 Buscar participante")
            print("4. ✅ Marcar presença")
            print("5. 📊 Gerar relatório")
            print("6. 📤 Exportar para CSV")
            print("7. 🚪 Sair")
            
            opcao = input("\nEscolha uma opção (1-7): ").strip()
            
            if opcao == '1':
                self.cadastrar_participante()
            elif opcao == '2':
                self.listar_participantes()
            elif opcao == '3':
                self.buscar_participante()
            elif opcao == '4':
                self.marcar_presenca()
            elif opcao == '5':
                self.gerar_relatorio()
            elif opcao == '6':
                self.exportar_para_csv()
            elif opcao == '7':
                print("\n👋 Obrigado por usar o sistema de registro!")
                print("Até logo! 🎉")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")

def main():
    """Função principal"""
    print("🎪 BEM-VINDO AO SISTEMA DE REGISTRO DE EVENTO!")
    print("Cadastre participantes com nome, e-mail e CPF.")
    
    sistema = SistemaEvento()
    sistema.menu_principal()

if __name__ == "__main__":
    main()