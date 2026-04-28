"""Metodos em listas são funções pré-definidas que podem ser usadas para realizar operações específicas em listas.
 Eles são chamados usando a sintaxe de ponto (.) após o nome da lista, seguido pelo nome"""


lista = [1, 2, 3, 4, 5]
lista.append(6)  # Adiciona o elemento 6 ao final da lista
print(lista)
lista.clear()  # Remove todos os elementos da lista
print(lista)
lista = [1, 2, 3, 4, 5]
l2 = lista.copy()  # Retorna uma cópia da lista
print(lista)

print(id(lista), id(l2))  # Verifica se as listas são diferentes objetos na memória

lista.count(2)  # Retorna o número de vezes que o elemento 2 aparece na lista
print(lista.count(2))

lista.extend([6, 7, 8])  # Adiciona os elementos 6, 7 e 8 ao final da lista
print(lista)


lista.pop()  # Remove e retorna o último elemento da lista
print(lista)
lista.pop(0)  # Remove e retorna o elemento no índice 0 (primeiro elemento)
print(lista)

lista.remove(3)  # Remove a primeira ocorrência do elemento 3 na lista
print(lista)


lista.reverse()  # Inverte a ordem dos elementos na lista
print(lista)

lista.sort(reverse=True)  # Ordena os elementos da lista em ordem decrescente
print(lista)

lista.sort(key=lambda x: x % 2)  # Ordena os elementos da lista com base no valor do resto da divisão por 2
print(lista)