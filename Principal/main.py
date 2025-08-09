import textwrap

def menu():
    menu = """ \n
    ========= MENU =========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Transferência
    [0] Sair
    ========================
    """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso! ===")
    else:
        print("A operação falhou! O valor inserido é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite,  numero_saques, limite_saques):
    ...

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        # Depósito
        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        

        # Saque
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

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
            exibir_extrato(saldo,extrato=extrato)

            print("\n=============== EXTRATO ===============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\n Saldo: R$ {saldo:.2f}")
            print("=========================================")

        # Criar conta
        elif opcao == "4":
            numero_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        # Listar contas
        elif opcao == "5":
            ...

        # Novo usuário
        elif opcao == "6":
            criar_usuario(usuarios)

        #Transferência
        elif opcao == "7":
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
        elif opcao == "0":
            print("Finalizando programa...")
            break

        else:
            print("Escolha uma opção válida!")
        

