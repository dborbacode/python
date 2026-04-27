""" Listas em python podem armazenar de maneira sequencial qualquer tipo de objeto, podemos criar listas utilizando o construtor list() ou utilizando colchetes []. 
Listas são mutáveis, ou seja, podemos alterar seus elementos. """

# Exemplos

frutas = []
frutas = ['maçã', 'banana', 'laranja']
print(frutas)

letras = list('python')
print(letras)

numeros = list(range(1, 11))
print(numeros)

carro = ['gol', 2010, 'preto', 4, True]
print(carro)

"""
Listas aninhadas são listas que contêm outras listas como elementos. Elas podem ser usadas para representar estruturas de dados mais complexas, como matrizes ou tabelas.
"""

matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(matriz)

print(matriz[0])  # Acessa a primeira linha da matriz
print(matriz[0][1])  # Acessa o elemento na primeira linha e segunda coluna (2)
print(matriz[0][-1])
print(matriz[-1][-1])


"""
Fatiamento de listas é uma técnica que permite acessar uma parte específica de uma lista,
utilizando a sintaxe de colchetes [] e os índices de início e fim. O índice de início é inclusivo, enquanto o índice de fim é exclusivo.  
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
print(numeros[0:5])  # Acessa os elementos do índice 0 ao 4
print(numeros[5:])   # Acessa os elementos do índice 5 até o final da lista
print(numeros[:5])   # Acessa os elementos do início da lista até o índice 4
print(numeros[::2])  # Acessa os elementos do início ao fim da lista, pulando de 2 em 2
print(numeros[::-1]) # Acessa os elementos do início ao fim da lista, mas na ordem inversa


for numero in numeros:
    print(numero)

carros = ['gol', 'palio', 'celta']

for indice, carro in enumerate(carros):
    print(f'{indice} - {carro}')


"""List comprehension é uma forma concisa de criar listas em Python. Ela permite criar uma nova lista a partir de uma sequência existente, 
aplicando uma expressão a cada elemento da sequência. A sintaxe básica é: [expressão for item in sequência if condição]."""

numeros = [1, 2, 3, 4, 5, 6,7]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)    

# list comprehension
pares_comprehension = [numero for numero in numeros if numero % 2 == 0]


print(pares, pares_comprehension)

# modificando valores 
numeros = [1, 2, 3, 4, 5]

numeros_ao_quadrado = [numero ** 2 for numero in numeros] 