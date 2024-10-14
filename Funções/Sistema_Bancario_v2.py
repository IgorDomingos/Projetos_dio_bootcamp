#Sistema Bancario

menu = """

------ MENU ------
Escolha uma opção:

    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

------------------

"""
deposito = 0
saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3
valor = 0

while True:
    comando = input(menu)

    if (comando == "d"):
        deposito = float(input("Por favor, informe o valor do depósito:\n"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f} efetuado.\n"
            print(f"O valor de {deposito:.2f} reais foi depositado com sucesso!\n")
        else:
            print("Operação cancelada! O valor informado é inválido.\n")
    elif (comando == "s"):
        if (numero_saques < LIMITES_SAQUES):
            saque = float(input("Por favor, informe o valor do saque:\n"))
            if (saque > 0 and saque <= limite):
                if (saque > saldo):
                    print ("Atenção, o saldo atual é menor que o valor de saque digitado!\n")
                else:
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque de R$ {saque:.2f} efetuado.\n"
                    print(f"Operação realizada, reitre o valor na boca do caixa.\n")
            elif (saque > limite):
                print("O valor digitado é superior ao limite de saque. Operação cancelada!\n")
            else:
                print("Operação cancelada! O valor informado é inválido.\n")
        else:
            print("Desculpe, a operação não poderá ser realizada, pois o limite de saques diários já foi atingido.\n")
    elif (comando == "e"):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif (comando == "q"):
        print("Saindo do sistema...")
        break
    else:
        print("Opção indisponível. Selecione uma opção válida!\n")
