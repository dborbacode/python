"""
metodos em dicionários são funções pré-definidas que permitem realizar operações específicas em dicionários, como adicionar, remover ou acessar elementos.
"""
contatos = {
    "contato.danielborba@gmail.com":{
        "nome": "Daniel",
        "telefone": "3333-4321"
    },
    }

copia = contatos.copy()
copia["contato.danielborba@gmail.com"]["telefone"] = "3333-1234"
print(copia)


print(contatos.get("contato.danielborba@gmail.com", "Chave não encontrada"))
"""
copy() é um método que cria uma cópia rasa do dicionário, ou seja, ele copia o dicionário, m
as os objetos dentro do dicionário ainda são referenciados. Portanto, se você modificar um objeto dentro do dicionário copiado, 
ele também modificará o objeto correspondente no dicionário original.

get() é um método que retorna o valor associado a uma chave específica. Se a chave não existir no dicionário, 
ele retorna um valor padrão (que pode ser especificado como segundo argumento) ou None se nenhum valor padrão for fornecido.

pop() é um método que remove um item do dicionário e retorna o valor associado à chave especificada. Se a chave não existir, ele pode lançar um KeyError
 ou retornar um valor padrão se fornecido

popitem() é um método que remove e retorna um par chave-valor aleatório do dicionário. Se o dicionário estiver vazio, ele pode lançar um KeyError.
"""