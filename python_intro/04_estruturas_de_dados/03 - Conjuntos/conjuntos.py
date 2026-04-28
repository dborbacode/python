"""conjuntos em python são estruturas de dados que armazenam elementos únicos e não ordenados.
Eles são definidos usando chaves {} ou a função set(). 
Os conjuntos são úteis para realizar operações matemáticas como união, interseção e diferença entre conjuntos.
"""

set([1,2,3,3,4,4,5]) # Criando um conjunto a partir de uma lista, os elementos duplicados serão removidos   

# Criando um conjunto usando chaves
meu_conjunto = {1, 2, 3, 4, 5}
print(meu_conjunto)

# com tupla

set(("palio", "gol", "celta", "palio")) # Criando um conjunto a partir de uma tupla, os elementos duplicados serão removidos

linguages = {"python", "java", "c++", "python"} # Criando um conjunto usando chaves, os elementos duplicados serão removidos
print(linguages)

for indice, carro in enumerate(linguages):
    print(f"{indice}: {carro}")



linguages = list(linguages) # Convertendo o conjunto para uma lista
print(linguages[0]) # Acessando o primeiro elemento da lista convertida do conjunto

"""
union() é um método que retorna um novo conjunto contendo todos os elementos de ambos os conjuntos, sem duplicatas.
"""

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

conjunto_union = conjunto_a.union(conjunto_b) # Realizando a união dos conjuntos
print(conjunto_union)

"""
intersection() é um método que retorna um novo conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos.
"""

conjunto_intersection = conjunto_a.intersection(conjunto_b) # Realizando a interseção dos conjuntos
print(conjunto_intersection)


"""
difference() é um método que retorna um novo conjunto contendo os elementos que estão presentes no primeiro conjunto, mas não no segundo.
"""
conjunto_difference = conjunto_a.difference(conjunto_b) # Realizando a diferença dos conjuntos
print(conjunto_difference)


"""
add() é um método que adiciona um elemento ao conjunto. Se o elemento já estiver presente, 
o conjunto permanecerá inalterado, pois os conjuntos não permitem elementos duplicados.
"""
sorteio = {1, 2, 3, 4, 5}
sorteio.add(6) # Adicionando um elemento ao conjunto
print(sorteio)