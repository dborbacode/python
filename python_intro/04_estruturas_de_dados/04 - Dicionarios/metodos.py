"""Metodos em dicionarios são funções que realizam operações específicas em dicionários. Eles permitem manipular, acessar e modificar os dados de forma eficiente. 
Alguns dos métodos mais comuns incluem: keys(), values(), items(), get(), update() e pop()."""

contatos = {"João": "joao@email.com", "Maria": "maria@email.com ", "Pedro": "pedro@gmail.com"}

contatos.clear()  # Limpa o dicionário, removendo todos os itens
print(contatos)  # Saída: {}    
copia_contatos = contatos.copy()   # Retorna uma cópia rasa do dicionário
print(copia_contatos)  # Saída: {}
print(contatos.get("João", "Contato não encontrado"))  # Saída: Contato não encontrado
dict.fromkeys(["João", "Maria", "Pedro"], "desconecido")  # Cria um novo dicionário com as chaves fornecidas e um valor padrão

contatos.update({"Ana": "ana@email.com"})  # Atualiza o dicionário com um novo par chave-valor
print(contatos)  # Saída: {"Ana": "ana@email.com"}