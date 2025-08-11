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
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo excedido!")

    elif excedeu_limite:
        print("Operação falhou! Limite de valor excedido!")

    elif excedeu_saques:
        print("Operação falhou! Limite de saques excedido!")

    elif valor <= 0:
        print("Operação falhou! O valor inserido é inválido")

    else:
        print("Operação saque realizada com sucesso!")
        saldo -= valor
        extrato += f"Saque no valor de {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realziado com sucesso!")
        

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):

    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def transferencia(contas, cpf_origem, cpf_destino, valor):
    def buscar_conta_por_cpf(contas, cpf):
        for conta in contas:
            if conta["usuario"]["cpf"] == cpf:
                return conta
        return None

    conta_origem = buscar_conta_por_cpf(contas, cpf_origem)
    conta_destino = buscar_conta_por_cpf(contas, cpf_destino)

    if not conta_origem:
        print("Conta de origem (CPF) não encontrada!")
        return False

    if not conta_destino:
        print("Conta de destino (CPF) não encontrada!")
        return False

    if valor <= 0:
        print("Valor inválido para transferência!")
        return False

    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente para transferência!")
        return False

    conta_origem["saldo"] -= valor
    conta_origem["extrato"] += f"Transferência enviada: R$ {valor:.2f} para CPF {cpf_destino}\n"

    conta_destino["saldo"] += valor
    conta_destino["extrato"] += f"Transferência recebida: R$ {valor:.2f} de CPF {cpf_origem}\n"

    print(f"Transferência de R$ {valor:.2f} de CPF {cpf_origem} para CPF {cpf_destino} realizada com sucesso!")
    return True

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

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )


        # Extrato
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)

            

        # Criar conta
        elif opcao == "4":
            numero_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_contas, usuarios)

            if conta:
                contas.append(conta)

        # Listar contas
        elif opcao == "5":
            listar_contas(contas)

            
        # Novo usuário
        elif opcao == "6":
            criar_usuario(usuarios)

        #Transferência
        elif opcao == "7":
            numero_origem = 1
            try:
                numero_destino = int(input("Digite o número da conta para transferência: "))
            except ValueError:
                print("Digite um número válido!")
                continue
            
            valor = float(input("Digite o valor da transferência: "))
            
            saldo, extrato = transferencia(contas, numero_origem, saldo, extrato, valor, numero_destino)

        # Sair
        elif opcao == "0":
            print("Finalizando programa...")
            break

        else:
            print("Escolha uma opção válida!")

main()
        

