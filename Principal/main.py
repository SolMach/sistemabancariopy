menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Transferência
[5] Sair

"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    # Depósito
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            print("Operação depósito realizada com sucesso!")
            saldo += valor
            extrato += f"Depósito no valor de {valor:.2f}\n"

        else:
            print("A operação terminou. O valor inserido é inválido.")
    

    # Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo excedido!")

        elif excedeu_limite:
            print("Operação falhou! Limite de valor excedido!")

        elif excedeu_saque:
            print("Operação falhou! Limite de saques excedido!")

        elif valor > 0:
            print("Operação saque realizada com sucesso!")
            saldo -= valor
            extrato += f"Saque no valor de {valor:.2f}\n"
            numero_saques += 1
            
        
        else: 
            print("Operação falhou! O valor inserido é inváido")


    # Extrato
    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================")


    #Transferência
    elif opcao == "4":
        numero = input("Digite o número da conta que deseja transferir: ")
        try:
            numero = int(numero)
            print(f"Transferência para número {numero} iniciada.")
        except ValueError:
            print("Digite apenas números inteiros!")
            continue
        

        valor = float(input("Digite o valor da transferência: "))

        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Saldo excedido!")
        
        elif valor > 0:
            print("Transferência feita com sucesso!")
            saldo -= valor
            numero_str = str(numero)
            ddd = numero_str[:2]
            resto = numero_str[2:]
            extrato += f"Transfêrencia no valor de {valor:.2f} para ({ddd}){resto}\n"

    # Sair
    elif opcao == "5":
        print("Finalizando programa...")
        break

    else:
        print("Escolha uma opção válida!")
        

