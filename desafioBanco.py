menu = """

[d] Depositar
[s] Sacar
[t] Transferir
[c] Consultar saldo
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido! O depósito deve ser positivo.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print("Valor do saque excede o limite de R$ 500,00.")
            elif valor > 0:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! O saque deve ser positivo.")
        else:
            print("Limite de saques diários atingido!")

    elif opcao == "t":
        valor = float(input("Informe o valor da transferência: "))
        if valor > saldo:
            print("Saldo insuficiente para a transferência!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
        else:
            print("Valor inválido! A transferência deve ser positiva.")

    elif opcao == "c":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "e":
        print("\n===== EXTRATO =====")
        print(extrato if extrato else "Nenhuma transação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida! Escolha uma opção do menu.")
