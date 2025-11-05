alunos = {}

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    alunos[nome] = []
    print(f"Aluno {nome} cadastrado!\n")

def lancar_notas():
    nome = input("Nome do aluno: ")
    if nome in alunos:
        try:
            nota = float(input("Nota: "))
            alunos[nome].append(nota)
            print("Nota lançada!\n")
        except:
            print("Nota inválida!\n")
    else:
        print("Aluno não encontrado!\n")

def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    return 0

def situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

def boletim():
    print("\n--- BOLETIM ---")
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: Notas {notas} | Média: {media:.1f} | {situacao(media)}")
    print()

# Menu principal
while True:
    print("1 - Cadastrar aluno")
    print("2 - Lançar nota")
    print("3 - Ver boletim")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        lancar_notas()
    elif opcao == '3':
        boletim()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")