faturamento_produtos = {
    "Notebook": 5500.00,
    "Teclado Mecânico": 350.00,
    "Monitor 4K": 2200.00,
    "Mouse Wireless": 150.00,
    "Headset Gamer": 450.00,
    "Suporte Articulado": 180.00
}

# Crie uma nova lista apenas com os nomes dos produtos que faturaram mais de R$ 400,00

lista_produtos = [] # iniciando a lista vazia

for chave, valor in faturamento_produtos.items():
    if valor > 400:
        lista_produtos.append(chave)

print(lista_produtos)  # Exibe a lista de produtos que faturaram mais de R$ 400,00

"""
Modifique o dicionário original aplicando um desconto fictício de 10%,
no valor de todos os produtos que faturaram menos de R$ 300,00.
"""

for chave, valor in faturamento_produtos.items():
    if valor < 300:
        faturamento_produtos[chave] = valor * 0.9
        
