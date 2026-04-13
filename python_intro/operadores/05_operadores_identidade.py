# Operadores de identidades são
# usados para comparar a identidade de objetos, ou seja, se dois objetos são o mesmo objeto na memória.

curso = "Python"
nome_curso = curso
saldo,limite = 200,100

curso is nome_curso # True, pois ambos apontam para o mesmo objeto na memória.
saldo is limite # False, pois são objetos diferentes na memória, mesmo que tenham o mesmo valor.

curso is not nome_curso # False, pois ambos apontam para o mesmo objeto na memória.
saldo is not limite # True, pois são objetos diferentes na memória, mesmo que tenham o mesmo valor.