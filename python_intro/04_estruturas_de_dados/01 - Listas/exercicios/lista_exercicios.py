
"""
1 - receba uma lista de números e retorne a soma de todos os números na lista.
"""
lista_numeros = [10,20,30,40,50]
soma_lista_numeros = sum(lista_numeros)
print(f"A soma dos números na lista é: {soma_lista_numeros}")

"""
2 - Peça 5 números ao usuário e armazene em uma lista.
Depois mostre:
maior número
menor número
"""

numeros_usuario = []
for i in range(5):
    numeros = int(input(f"Digite o número {i+1}: "))
    numeros_usuario.append(numeros)

print(f"O maior número é: {max(numeros_usuario)}")
print(f"O menor número é: {min(numeros_usuario)}")


"""
3 - Crie uma lista de nomes e imprima cada nome em uma linha. 
"""
nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for nome in nomes:
    print(nome) 

"""
4 - Contar itens, conte a quantidade que tem da palavra "arroz" em uma lista de alimentos.
"""

lista_alimentos = ["arroz", "feijão", "arroz", "macarrão", "arroz", "carne"]
quantidade_arroz = lista_alimentos.count("arroz")
print(f"A palavra 'arroz' aparece {quantidade_arroz} vezes na lista de alimentos.")

"""
5 - inverter a lista, crie uma lista de números e imprima a lista invertida.
"""
numeros = [1, 2, 3, 4, 5]
numeros_invertidos = numeros[::-1]
print(f"A lista original é: {numeros}")
print(f"A lista invertida é: {numeros_invertidos}")

"""
6 - remover duplicados, crie uma lista de números com alguns números repetidos e imprima a lista sem os números duplicados. 
"""

lista_duplicados = [1, 2, 3, 2, 4, 5, 1, 6]
lista_sem_duplicados = list(set(lista_duplicados))
print(f"A lista original é: {lista_duplicados}") 
print(f"A lista sem duplicados é: {lista_sem_duplicados}")

"""
7 - ordenar a lista, crie uma lista de números e imprima a lista ordenada em ordem crescente.
"""
numeros_desordenados = [5, 2, 9, 1, 5, 6]
numeros_ordenados = sorted(numeros_desordenados)
print(f"A lista original é: {numeros_desordenados}")
print(f"A lista ordenada é: {numeros_ordenados}")

"""
8 - Pares, crie uma lista de números e imprima apenas os números pares da lista.
"""

numeros_pares = []

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
        print(num)
print(f"Os números pares na lista são: {numeros_pares}")


"""
9 - Buscar item - crie uma lista de nomes e peça ao usuário para digitar um nome. Verifique se o nome está na lista e imprima uma mensagem apropriada.
"""

lista_nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
nome_busca = input("Digite um nome para buscar na lista: ")
if nome_busca in lista_nomes:
    print(f"O nome '{nome_busca}' está na lista.")
else:
    print(f"O nome '{nome_busca}' não está na lista.")


"""
10 - Separar aprovados e reprovados - crie uma lista de notas e
 separe os alunos aprovados (nota >= 60) dos reprovados (nota < 60). Imprima as duas listas.
"""

lista_aprovados = []
lista_reprovados = []

lista_notas = [75, 45, 82, 59, 90, 30, 68]

for nota in lista_notas:
    if nota >= 60:
        lista_aprovados.append(nota)
    else:
        lista_reprovados.append(nota)

print(f"Os alunos aprovados são: {lista_aprovados}")
print(f"Os alunos reprovados são: {lista_reprovados}")


"""
11 - simular contagem de logs da api no sistema. E contar quantas vezes cada status code aparece na lista de logs.
"""

logs_api = ["200 OK", "404 Not Found", "500 Internal Server Error", "200 OK", "403 Forbidden"]

status_code_count = {}
for log in logs_api:
    status_code = log.split()[0]  # Extrai o status code do log
    if status_code in status_code_count:
        status_code_count[status_code] += 1
    else:
        status_code_count[status_code] = 1

print("Contagem de logs por status code:")
for status_code, count in status_code_count.items():
    print(f"{status_code}: {count}")

"""
12 - contar usuários duplicados, crie uma lista de usuários com alguns nomes repetidos e conte quantas vezes cada nome aparece na lista.
"""

usuarios = ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Eve"]

for usuario in set(usuarios):
    count = usuarios.count(usuario)
    print(f"O nome '{usuario}' aparece {count} vezes na lista de usuários.")

"""
13 - Extrair domínios de e-mails, crie uma lista de endereços de e-mail e extraia os domínios (parte após o @) para uma nova lista.
"""
lista_emails = ["dan@gmail.com", "maria@yahoo.com", "joao@outlook.com", "ana@company.org"]
dominios = [email.split("@")[1] for email in lista_emails]
print(f"Os domínios extraídos são: {dominios}")