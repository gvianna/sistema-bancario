menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
extract = ""
number_withdraw = 0
LIMIT_WITHDRAW = 3
remaining_withdraw = 0

while True:

    remaining_withdraw = LIMIT_WITHDRAW - number_withdraw
    max(0, remaining_withdraw)
    option = input(menu)

    if option == "d":
        print("Depósito\n")
        deposit_value = float(input("Informe o valor do depósito: "))
        balance += deposit_value
        extract += f" + R$ {deposit_value:.2f} OP. [d] Depósito \n"
        print("Operação realizada com sucesso.")

    elif option == "s":
        print("Saque\n")
        if remaining_withdraw == 0:
            status = "Quantidade máxima de saques diários atingida."
            print(status)
        else:
            withdraw = float(input("Informe o valor do saque: "))

            if withdraw > limit and withdraw > balance:
                status = "Valor do saque é maior que o saldo em conta e ultrapassa o limite por saque individual."
            elif withdraw > limit:
                status = "Saque ultrapassa o limite por saque."
            elif withdraw > balance:
                status = "Saque excede o saldo em conta."
        
            if balance >= withdraw and withdraw <= limit and remaining_withdraw != 0:    
                print(f"Saque de R${withdraw} realizado com sucesso.")
                number_withdraw += 1
                extract += f" - R$ {withdraw} OP. [s] Saque \n"
                balance -= withdraw
            else:
                print(f"Falha ao sacar, {status}")

    elif option == "e":
        print("Extrato\n")
        print(f"Seu saldo atual é de R${balance}\n Seu limite de saques diários restante: {remaining_withdraw}")
        print(extract)
        
    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")