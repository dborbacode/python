"""Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, o que significa que você pode adicionar, 
remover ou modificar os itens após a criação do dicionário. 
As chaves em um dicionário devem ser únicas e imutáveis (como strings, números ou tuplas), enquanto os valores podem ser de qualquer tipo de dado."""


pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

pessoa = dict(nome="João", idade=30, cidade="São Paulo")

pessoa["profissao"] = "Engenheiro de dados"

print(pessoa)

"""Dicionarios ainhados Dicionários podem conter outros dicionários como valores, permitindo a criação de estruturas de dados mais complexas."""
empresa = {
    "nome": "Tech Solutions",
    "funcionarios": {  "João": {"idade": 30, "cargo": "Engenheiro de dados"},
                       "Maria": {"idade": 25, "cargo": "Analista de dados"} }
}

print(empresa["funcionarios"]["João"]["cargo"])  # Saída: Engenheiro de dados


for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")