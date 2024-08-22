SALDO = 500
LIMITE_SAQUES = 3
numero_saques = 0
extrato_transacoes = []

menu = """
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
"""

def depositar(deposito):
    global SALDO
    if deposito > 0:
        SALDO += deposito
        extrato_transacoes.append(f"Depósito: +{deposito:.2f}")
    else:
        print("Valor de depósito inválido!")

def sacar(saque):
    global SALDO
    global numero_saques
    if numero_saques < LIMITE_SAQUES:
        if saque > 0 and saque <= SALDO:
            SALDO -= saque
            numero_saques += 1
            extrato_transacoes.append(f"Saque: -{saque:.2f}")
        elif saque > SALDO:
            print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido!")
    else:
        print("Limite de saques atingido!")

def extrato():
    print("\nExtrato:")
    for transacao in extrato_transacoes:
        print(transacao)
    print(f"Saldo atual: {SALDO:.2f}\n")

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor para depósito: "))
        depositar(valor_deposito)
    elif opcao == "2":
        valor_saque = float(input("Digite o valor para saque: "))
        sacar(valor_saque)
    elif opcao == "3":
        extrato()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
