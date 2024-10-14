#Sistema Bancario_Versão_2

def menu():
    menu = """\n
    ========= MENU =========
    Escolha uma opção:

    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [lc] Listar Contas
    [q] Sair
    
    ========================
    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f} efetuado.\n"
        print(f"O valor de {valor:.2f} reais foi depositado com sucesso!\n")
    else:
        print("Operação cancelada! O valor informado é inválido.\n")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (numero_saques < limite_saques):
        if (valor > 0 and saque <= limite):
            if (valor > saldo):
                print("Atenção, o saldo atual é menor que o valor de saque digitado!\n")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque de R$ {saque:.2f} efetuado.\n"
                print(f"Operação realizada, reitre o valor na boca do caixa.\n")
        elif (valor > limite):
            print("O valor digitado é superior ao limite de saque. Operação cancelada!\n")
        else:
            print("Operação cancelada! O valor informado é inválido.\n")
    else:
        print("Desculpe, a operação não poderá ser realizada, pois o limite de saques diários já foi atingido.\n")

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuarios):
    cpf = input("Por favor, informe o seu CPF (apenas números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Erro! Já existe um usuário com este CPF.")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço, no formato: (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Parabéns! Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Atenção, usuário não encontrado! Operação de criação de conta encerrada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Nº_Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []

    valor = 0

    while True:
        comando = menu()

        if (comando == "d"):
            valor = float(input("Por favor, informe o valor do depósito:\n"))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif (comando == "s"):
            valor = float(input("Por favor, informe o valor do saque:\n"))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITES_SAQUES,
            )
        elif (comando == "e"):
            extrato(saldo, extrato=extrato)
        elif (comando == "nu"):
            novo_usuario(usuarios)
        elif (comando == "nc"):
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif (comando == "lc"):
            listar_contas(contas)
        elif (comando == "q"):
            print("Saindo do sistema...")
            break
        else:
            print("Opção indisponível. Selecione uma opção válida!\n")

main()