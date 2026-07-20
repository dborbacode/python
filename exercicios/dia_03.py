
# ==========================================================
# BLOCO 5 - DICIONÁRIOS
# ==========================================================

def contar_letras(palavra):
    """
    Recebe uma palavra (string).
    Retorna um dicionário onde a chave é a letra e o valor é
    quantas vezes ela aparece na palavra.

    Exemplo:
        contar_letras("banana") -> {'b': 1, 'a': 3, 'n': 2}
    """
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

dicionario_words = contar_letras("Banana")
print(dicionario_words)

def inverter_dicionario(dicionario):
    """
    Recebe um dicionário simples (chave: valor, sem repetir valores).
    Retorna um novo dicionário com chave e valor invertidos.

    Exemplo:
        inverter_dicionario({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
    """
    dicionario_invertido = {}

    for chave, valor in dicionario.items():
        dicionario_invertido[valor] = chave
       




def maior_valor_dicionario(dicionario):
    """
    Recebe um dicionário onde os valores são números.
    Retorna a CHAVE que tem o maior valor.

    Exemplo:
        maior_valor_dicionario({'joao': 85, 'maria': 92, 'ana': 78})
        -> 'maria'
    """
    maior_chave = None
    maior_valor = None

    for chave, valor in dicionario.items():
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            maior_chave = chave

    return maior_chave
   
