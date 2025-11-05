import json
import hashlib
import os

class LoginSimples:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()
        self.logado = None
    
    def carregar_usuarios(self):
        try:
            with open('usuarios_simples.json', 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def salvar_usuarios(self):
        with open('usuarios_simples.json', 'w') as f:
            json.dump(self.usuarios, f, indent=2)
    
    def hash_senha(self, senha):
        return hashlib.md5(senha.encode()).hexdigest()
    
    def cadastrar(self):
        print("\n--- CADASTRO ---")
        usuario = input("Usuário: ")
        
        if usuario in self.usuarios:
            print("❌ Usuário já existe!")
            return
        
        senha = input("Senha: ")
        self.usuarios[usuario] = self.hash_senha(senha)
        self.salvar_usuarios()
        print("✅ Cadastrado com sucesso!")
    
    def login(self):
        print("\n--- LOGIN ---")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        if usuario in self.usuarios and self.usuarios[usuario] == self.hash_senha(senha):
            self.logado = usuario
            print(f"✅ Login bem-sucedido! Bem-vindo, {usuario}!")
            return True
        else:
            print("❌ Usuário ou senha incorretos!")
            return False
    
    def menu(self):
        while True:
            print(f"\n{'--- LOGADO: ' + self.logado if self.logado else '--- SISTEMA LOGIN ---'}")
            print("1. Cadastrar")
            print("2. Login")
            print("3. Sair")
            
            if self.logado:
                print("4. Logout")
            
            opcao = input("Opção: ")
            
            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                self.login()
            elif opcao == '3':
                print("👋 Até logo!")
                break
            elif opcao == '4' and self.logado:
                print(f"👋 Até logo, {self.logado}!")
                self.logado = None
            else:
                print("❌ Opção inválida!")

if __name__ == "__main__":
    sistema = LoginSimples()
    sistema.menu()