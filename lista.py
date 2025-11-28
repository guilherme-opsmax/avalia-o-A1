alunos = []

print("=== Cadastro de Alunos ===")
print("Digite 'sair' para encerrar.\n")

while True:
    nome = input("Digite o nome do aluno: ")

    if nome.lower() == "sair":
        break

    alunos.append(nome)

print("\n=== Lista de Alunos Cadastrados ===")
for aluno in alunos:
    print(f"- {aluno}")
