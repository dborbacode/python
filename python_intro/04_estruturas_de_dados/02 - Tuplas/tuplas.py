"""
Tuplas são estruturas de dados imutáveis, ou seja, uma vez criadas, seus elementos não podem ser alterados.
 Elas são semelhantes às listas, mas com a diferença de que as tuplas são definidas usando parênteses () em vez de colchetes [].
"""
# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)
letras = tuple(['a', 'b', 'c', 'd', 'e'])  # Criando uma tupla a partir de uma lista
print(minha_tupla)
print(letras)


# Acessando elementos de uma tupla
print(minha_tupla[-1])  # Acessando o primeiro elemento

""""
Tuplas aninhadas são tuplas que contêm outras tuplas como elementos. Elas permitem criar estruturas de dados mais complexas e organizadas.
"""

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

matriz[0]  # Acessando a primeira linha da matriz
matriz[1][2]  # Acessando o elemento na segunda linha e terceira


"""
fatiamento de tuplas é semelhante ao fatiamento de listas, permitindo acessar uma parte da tupla usando índices e intervalos.
"""

minha_tupla[1:4]  # Acessando os elementos do índice 1 ao 3
letras[:3]  # Acessando os primeiros três elementos