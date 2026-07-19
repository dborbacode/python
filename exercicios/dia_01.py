"""
LISTA DE EXERCÍCIOS COMBINADOS - PYTHON
Assuntos: listas, list comprehension, fatiamento, tuplas, if/else,
dicionários, estruturas aninhadas, input(), while, funções.

Como usar:
- Cada exercício é uma função com docstring explicando o que fazer.
- Apague o "pass" e escreva sua solução no lugar.
- Teste chamando a função na área de testes no final do arquivo.
- Comece do exercício 1 e vá subindo — a dificuldade é progressiva.
"""


# ==========================================================
# BLOCO 1 - LISTAS + IF/ELSE + FUNÇÕES
# ==========================================================

def maiores_que(lista, limite):
    """
    Recebe uma lista de números e um valor limite.
    Retorna uma NOVA lista contendo apenas os números maiores que o limite.

    Exemplo:
        maiores_que([1, 5, 10, 15, 20], 10) -> [15, 20]
    """
    lista_maiores = []
    for i in lista:
        if i > limite:
            lista_maiores.append(i)

    return lista_maiores

teste_numeros = maiores_que([1,2,3,4,5,6,7,8], 4)
print(teste_numeros)




def separar_pares_impares(lista):
    """
    Recebe uma lista de números.
    Retorna DUAS listas: uma com os pares e outra com os ímpares.
    (dica: pode retornar uma tupla com as duas listas: return pares, impares)

    Exemplo:
        separar_pares_impares([1, 2, 3, 4, 5]) -> ([2, 4], [1, 3, 5])
    """
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else: 
            impares.append(i)
    return pares,impares
        
teste_pares_impares = separar_pares_impares([1,2,3,4,5,6])
print(teste_pares_impares)

        


def remover_duplicados(lista):
    """
    Recebe uma lista (pode ter números repetidos).
    Retorna uma nova lista sem elementos duplicados, mantendo a ordem original.

    Exemplo:
        remover_duplicados([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
    """
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado 

print(remover_duplicados([1,2,3,4,5,6,6,6,7,8,99]))

    
# ==========================================================
# BLOCO 2 - LIST COMPREHENSION
# ==========================================================

def quadrados(lista):
    """
    Usando LIST COMPREHENSION, retorne uma lista com o quadrado
    de cada número da lista recebida.

    Exemplo:
        quadrados([1, 2, 3, 4]) -> [1, 4, 9, 16]
    """
    quadrado = [i * 2 for i in lista]
    return quadrado 
print(quadrados([1,2,3,4]))
    

def apenas_pares_comprehension(lista):
    """
    Usando LIST COMPREHENSION (com condição if dentro), retorne
    apenas os números pares da lista.

    Exemplo:
        apenas_pares_comprehension([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    """
    pares = [i for i in lista if i % 2 == 0]
    return pares 
print(apenas_pares_comprehension([1,3,5,7,9,8,10,1,2,16,18,32,24,56]))




def primeiras_letras(lista_palavras):
    """
    Usando LIST COMPREHENSION, retorne uma lista só com a primeira
    letra de cada palavra da lista recebida.

    Exemplo:
        primeiras_letras(['casa', 'bola', 'time']) -> ['c', 'b', 't']
    """
    primeira = [i[0] for i in lista_palavras]
    return primeira 
print(primeiras_letras(['acabou', 'bacana']))
