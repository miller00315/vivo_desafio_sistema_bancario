menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

saldo = 0

numeros_saques = 0

extrato = ""

limite_saque = 500

LIMITE_SAQUES = 3

mensagem_erro = "Operação falhou: "

while True:
    opcao = input(menu)

    match opcao:
        case "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print(mensagem_erro + "o valor informado é inválido.")

        case "s":
            valor = float(input("Informe o valor do saque."))

            excedeu_saldo  = valor > saldo

            excedeu_limite = valor > limite_saque

            excedeu_saque = numeros_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print(mensagem_erro + "saldo insuficiente.")

            elif excedeu_limite:
                print(mensagem_erro + "excedu o valor limite de saque.")

            elif excedeu_saque:
                print(mensagem_erro + "excedeu o limite de sque diário.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numeros_saques += 1
            else:
                print("Operação falhou: o valor informado é inválido.")
        
        case "e":
            print("\n=================== EXTRATO ================")
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("============================================")

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a opção desejada")