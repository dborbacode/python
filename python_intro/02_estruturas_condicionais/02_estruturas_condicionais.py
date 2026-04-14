
idade = 19
habilitado = True 

permissao_para_dirigir = idade >= 18 and habilitado

if permissao_para_dirigir == True: 
    print("Você tem permissão para dirigir.")

# if/else/elif serve para criar estruturas condicionais mais complexas, onde podemos ter múltiplas condições e ações diferentes para cada uma delas.

opcao = int(input("Escolha uma opção (1, 2 ou 3): "))

if opcao == 1:
    print("Você escolheu a opção 1.")
elif opcao == 2:
    print("Você escolheu a opção 2.")
elif opcao == 3:
    print("Você escolheu a opção 3.")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

#ifs aninhados são estruturas condicionais onde temos um if dentro de outro if. Eles são usados para verificar múltiplas condições de forma hierárquica.

conta_normal = True 
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 1000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado usando cheque especial.")
    else:
        print("Saldo insuficiente para saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente para saque.")

#if ternário é uma forma compacta de escrever uma estrutura condicional simples. Ele permite que você atribua um valor a uma variável com base em uma condição, tudo em uma única linha.
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status) # Maior de idade