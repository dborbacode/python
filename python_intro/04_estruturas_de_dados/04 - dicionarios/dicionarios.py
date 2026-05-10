"""
Um dicionários é um conjunto não ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionários.
"""
pessoa = {"nome":"Daniel", "idade": 26}

pessoa = dict(nome="guilherme", idade=28)

pessoa["telefone"] = "3333-1234"

print(pessoa)

pessoa["telefone"] = "3333-4321"
print(pessoa)


"""
dicionários aninhados são dicionários dentro de dicionários, ou seja, um dicionário pode conter outro dicionário como valor de uma chave.
"""
pessoa = {
    "nome": "Daniel",
    "idade": 26,
    "endereco": {
        "rua": "Rua A",
        "numero": 123,
        "cidade": "São Paulo"
    }
}
print(pessoa["endereco"]["rua"])


for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")