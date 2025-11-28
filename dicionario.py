# Lista que armazenará todos os produtos cadastrados
produtos = []

print("=== Sistema de Cadastro de Produtos ===")
print("Digite 'sair' no nome para encerrar.\n")

while True:
    # Solicita o nome do produto ao usuário
    nome = input("Nome do produto: ")

    # Se o usuário digitar "sair", o loop é encerrado
    if nome.lower() == "sair":
        break

    try:
        # Tenta converter o preço digitado para número (float)
        preco = float(input("Preço do produto (R$): "))
    except ValueError:
        # Caso o usuário digite algo que não é número, exibe erro e volta ao início do loop
        print("Preço inválido! Digite apenas números.")
        continue

    # Cria um dicionário representando o produto
    produto = {
        "nome": nome,
        "preco": preco
    }

    # Adiciona o produto na lista
    produtos.append(produto)
    print("Produto cadastrado!\n")

# Exibe todos os produtos cadastrados
print("\n=== Lista de Produtos Cadastrados ===")
for p in produtos:
    # Mostra cada produto com o nome e preço formatado com duas casas decimais
    print(f"- {p['nome']} | R$ {p['preco']:.2f}")
