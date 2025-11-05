class Participante:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
    
    def __str__(self):
        return f"Nome: {self.nome} | E-mail: {self.email} | CPF: {self.cpf}"

class SistemaEvento:
    def __init__(self):
        self.participantes = []
    
    def validar_cpf(self, cpf):
        """Valida se o CPF tem 11 dígitos numéricos"""
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        return len(cpf_limpo) == 11
    
    def validar_email(self, email):
        """Validação básica de e-mail"""
        return '@' in email and '.' in email
    
    def cpf_existe(self, cpf):
        """Verifica se o CPF já está cadastrado"""
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        for participante in self.participantes:
            participante_cpf_limpo = ''.join(filter(str.isdigit, participante.cpf))
            if participante_cpf_limpo == cpf_limpo:
                return True
        return False
    
    def cadastrar_participante(self):
        """Cadastra um novo participante"""
        print("\n" + "="*50)
        print("CADASTRO DE PARTICIPANTE")
        print("="*50)
        
        # Nome
        nome = input("Digite o nome completo: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        # E-mail
        email = input("Digite o e-mail: ").strip()
        if not self.validar_email(email):
            print("❌ E-mail inválido!")
            return
        
        # CPF
        cpf = input("Digite o CPF (apenas números): ").strip()
        if not self.validar_cpf(cpf):
            print("❌ CPF inválido! Deve conter 11 dígitos.")
            return
        
        if self.cpf_existe(cpf):
            print("❌ Este CPF já está cadastrado!")
            return
        
        # Criar e adicionar participante
        participante = Participante(nome, email, cpf)
        self.participantes.append(participante)
        print(f"✅ Participante {nome} cadastrado com sucesso!")
    
    def listar_participantes(self):
        """Lista todos os participantes cadastrados"""
        print("\n" + "="*50)
        print("LISTA DE PARTICIPANTES")
        print("="*50)
        
        if not self.participantes:
            print("Nenhum participante cadastrado.")
            return
        
        for i, participante in enumerate(self.participantes, 1):
            print(f"{i}. {participante}")
    
    def exibir_estatisticas(self):
        """Exibe estatísticas do evento"""
        print("\n" + "="*50)
        print("ESTATÍSTICAS DO EVENTO")
        print("="*50)
        print(f"📊 Total de inscritos: {len(self.participantes)}")
    
    def menu_principal(self):
        """Menu principal do sistema"""
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE REGISTRO DE EVENTOS")
            print("="*50)
            print("1. Cadastrar participante")
            print("2. Listar participantes")
            print("3. Ver estatísticas")
            print("4. Sair")
            print("="*50)
            
            opcao = input("Escolha uma opção (1-4): ").strip()
            
            if opcao == '1':
                self.cadastrar_participante()
            elif opcao == '2':
                self.listar_participantes()
            elif opcao == '3':
                self.exibir_estatisticas()
            elif opcao == '4':
                print("\nObrigado por usar o sistema!")
                print(f"Total final de inscritos: {len(self.participantes)}")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")

# Versão simplificada (alternativa)
def sistema_simplificado():
    """Versão simplificada do sistema"""
    participantes = []
    
    print("SISTEMA DE CADASTRO DE PARTICIPANTES")
    print("Digite 'sair' a qualquer momento para finalizar\n")
    
    while True:
        print("\nNovo Cadastro:")
        nome = input("Nome: ").strip()
        
        if nome.lower() == 'sair':
            break
        
        email = input("E-mail: ").strip()
        if email.lower() == 'sair':
            break
        
        cpf = input("CPF: ").strip()
        if cpf.lower() == 'sair':
            break
        
        if nome and email and cpf:
            participante = {
                'nome': nome,
                'email': email,
                'cpf': cpf
            }
            participantes.append(participante)
            print("✅ Participante cadastrado com sucesso!")
        else:
            print("❌ Todos os campos são obrigatórios!")
    
    # Exibir resultados
    print("\n" + "="*50)
    print("RESUMO FINAL")
    print("="*50)
    print(f"Total de participantes inscritos: {len(participantes)}")
    
    if participantes:
        print("\nLista de participantes:")
        for i, participante in enumerate(participantes, 1):
            print(f"{i}. {participante['nome']} - {participante['email']} - {participante['cpf']}")

# Execução principal
if __name__ == "__main__":
    print("Escolha a versão do sistema:")
    print("1. Sistema Completo (com menu)")
    print("2. Sistema Simplificado")
    
    escolha = input("Digite 1 ou 2: ").strip()
    
    if escolha == '1':
        sistema = SistemaEvento()
        sistema.menu_principal()
    else:
        sistema_simplificado()