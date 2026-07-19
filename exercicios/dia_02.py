# ==========================================================
# BLOCO 3 - FATIAMENTO DE LISTAS (SLICING)
# ==========================================================

def primeiros_e_ultimos(lista, quantidade):
    """
    Recebe uma lista e uma quantidade "n".
    Retorna uma tupla com (os "n" primeiros elementos, os "n" últimos elementos).
    Use FATIAMENTO (slicing), sem laços.

    Exemplo:
        primeiros_e_ultimos([1, 2, 3, 4, 5, 6, 7, 8], 3)
        -> ([1, 2, 3], [6, 7, 8])
    """
    primeira_parte = lista[:quantidade]
    segunda_parte = lista[-quantidade:]

    return primeira_parte, segunda_parte
    


def inverter_lista(lista):
    """
    Retorna a lista invertida, usando FATIAMENTO (ex: lista[::-1]).
    Não use a função reverse() nem o for.

    Exemplo:
        inverter_lista([1, 2, 3, 4]) -> [4, 3, 2, 1]
    """
    lista_invertida = lista[::-1]
    return lista_invertida

print(inverter_lista([1,2,3,4,5,6,7,8,9,10]))


def elementos_do_meio(lista):
    """
    Retorna os elementos do "miolo" da lista, removendo o primeiro
    e o último elemento. Use fatiamento.

    Exemplo:
        elementos_do_meio([1, 2, 3, 4, 5]) -> [2, 3, 4]
    """
    miolo_lista = lista[1:-1]

    return miolo_lista


# ==========================================================
# BLOCO 4 - TUPLAS
# ==========================================================

def coordenadas_distancia(ponto1, ponto2):
    """
    Recebe duas tuplas representando coordenadas (x, y).
    Retorna a distância entre elas (fórmula: raiz((x2-x1)^2 + (y2-y1)^2)).
    Dica: use "** 0.5" para fazer raiz quadrada, ou importe math.sqrt.

    Exemplo:
        coordenadas_distancia((0, 0), (3, 4)) -> 5.0
    """
    calculo_x = (ponto1[0] - ponto2[0]) **2
   

    calculo_y = (ponto1[1] - ponto2[1]) ** 2
   
    soma = calculo_x + calculo_y
    distancia = soma ** 0.5

    return distancia



def trocar_valores(tupla):
    """
    Recebe uma tupla com 2 elementos (a, b).
    Retorna uma NOVA tupla com os valores trocados (b, a).

    Exemplo:
        trocar_valores((1, 2)) -> (2, 1)
    """
    nova_tupla = (tupla[1], tupla[0])

    return nova_tupla
