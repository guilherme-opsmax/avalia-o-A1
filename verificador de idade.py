def verificar_idade():
    print("=== Sistema de Verificação de Idade ===")

    nome = input("Digite seu nome: ")
    
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida! Digite apenas números.")
        return

    print("\nClassificações do evento:")
    print("1 - Evento Livre (qualquer idade)")
    print("2 - Evento 12+")
    print("3 - Evento 16+")
    print("4 - Evento 18+")

    opcao = input("\nEscolha o tipo do evento (1-4): ")

    if opcao == "1":
        print(f"\n✔ {nome}, você pode entrar no evento livre!")
    elif opcao == "2":
        if idade >= 12:
            print(f"\n✔ {nome}, você pode entrar no evento 12+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 12 anos.")
    elif opcao == "3":
        if idade >= 16:
            print(f"\n✔ {nome}, você pode entrar no evento 16+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 16 anos.")
    elif opcao == "4":
        if idade >= 18:
            print(f"\n✔ {nome}, você pode entrar no evento 18+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 18 anos.")
    else:
        print("\nOpção inválida!")


verificar_idade()
