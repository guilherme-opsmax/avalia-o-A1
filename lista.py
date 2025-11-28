# Lista que armazenará os nomes dos alunos cadastrados
alunos = []

# Mensagens iniciais do sistema
print("=== Cadastro de Alunos ===")
print("Digite 'sair' para encerrar.\n")

while True:
    # Solicita ao usuário o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Verifica se o usuário deseja encerrar o cadastro
    if nome.lower() == "sair":
        break

    # Adiciona o nome do aluno na lista
    alunos.append(nome)

# Exibe a lista completa de alunos cadastrados
print("\n=== Lista de Alunos Cadastrados ===")
for aluno in alunos:
    # Mostra cada aluno individualmente
    print(f"- {aluno}")
