turma = [
    {
        "nome": "Ana",
        "disciplina": "Programação",
        "notas": [8.5, 9.0, 7.5, 10.0]
    },
    {
        "nome": "Bruno",
        "disciplina": "Programação",
        "notas": [6.0, 5.5, 7.0, 6.5]
    },
    {
        "nome": "Carla",
        "disciplina": "Programação",
        "notas": [9.5, 10.0, 9.8, 10.0]
    }
]


# Calcule a média das notas de cada aluno.
for aluno in turma:
   notas = aluno['notas']
   media = sum(aluno["notas"]) / len(aluno)
   print(f'A média é de {media:.2f}')
      
