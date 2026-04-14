saldo = 1000
saque = 200
limite = 100 

saldo >= saque and saque <= limite # True, pois o saldo é suficiente para o saque e o saque está dentro do limite permitido.
saldo >= saque or saque <= limite # True, pois o saldo é suficiente para o saque, mesmo que o saque esteja acima do limite permitido.
not(saldo >= saque) # False, pois o saldo é suficiente para o saque, então a negação é falsa.   

contatos_emergencia = ["Alice", "Bob", "Charlie"]
not contatos_emergencia # False, pois a lista de contatos de emergência não está vazia, então a negação é falsa.


