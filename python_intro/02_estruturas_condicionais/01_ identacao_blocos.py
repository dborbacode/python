def sacar(valor):
    saldo = 1000


    if saldo >= valor:
        saldo -= valor
        print(f'Saque de R${valor} realizado com sucesso. Saldo atual: R${saldo}')

    print('Obrigado por usar nosso serviço!')

sacar(100) # Saque de R$200 realizado com sucesso. Saldo atual: R$800

def depositar(valor):
    saldo = 1000

    if valor > 0:
        saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso. Saldo atual: R${saldo}')

    print('Obrigado por usar nosso serviço!')

depositar(500) # Depósito de R$500 realizado com sucesso. Saldo atual: R$1500