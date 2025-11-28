# Função responsável por verificar idade e liberar ou não a entrada no evento
def verificar_idade():
    print("=== Sistema de Verificação de Idade ===")

    # Solicita o nome do usuário
    nome = input("Digite seu nome: ")
    
    try:
        # Tenta converter a idade digitada para inteiro
        idade = int(input("Digite sua idade: "))
    except ValueError:
        # Caso não seja número, exibe erro e interrompe a função
        print("Idade inválida! Digite apenas números.")
        return

    # Exibe os tipos de eventos disponíveis
    print("\nClassificações do evento:")
    print("1 - Evento Livre (qualquer idade)")
    print("2 - Evento 12+")
    print("3 - Evento 16+")
    print("4 - Evento 18+")

    # Usuário escolhe o tipo de evento
    opcao = input("\nEscolha o tipo do evento (1-4): ")

    # Verificações baseadas na opção escolhida
    if opcao == "1":
        # Evento livre permite qualquer idade
        print(f"\n✔ {nome}, você pode entrar no evento livre!")
    
    elif opcao == "2":
        # Evento para maiores de 12
        if idade >= 12:
            print(f"\n✔ {nome}, você pode entrar no evento 12+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 12 anos.")
    
    elif opcao == "3":
        # Evento para maiores de 16
        if idade >= 16:
            print(f"\n✔ {nome}, você pode entrar no evento 16+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 16 anos.")
    
    elif opcao == "4":
        # Evento para maiores de 18
        if idade >= 18:
            print(f"\n✔ {nome}, você pode entrar no evento 18+!")
        else:
            print(f"\n❌ {nome}, você NÃO pode entrar. Idade mínima: 18 anos.")
    
    else:
        # Caso o usuário escolha algo fora de 1-4
        print("\nOpção inválida!")

# Chamada da função para executar o programa
verificar_idade()
