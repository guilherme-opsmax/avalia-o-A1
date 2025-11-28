produtos = []

print("=== Sistema de Cadastro de Produtos ===")
print("Digite 'sair' no nome para encerrar.\n")

while True:
    nome = input("Nome do produto: ")

    if nome.lower() == "sair":
        break

    try:
        preco = float(input("Preço do produto (R$): "))
    except ValueError:
        print("Preço inválido! Digite apenas números.")
        continue

    produto = {
        "nome": nome,
        "preco": preco
    }

    produtos.append(produto)
    print("Produto cadastrado!\n")

print("\n=== Lista de Produtos Cadastrados ===")
for p in produtos:
    print(f"- {p['nome']} | R$ {p['preco']:.2f}")
