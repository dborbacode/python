idade = int(input('Digite a idade do nadador: '))

if idade == 5 and idade <= 7:
    print('Infantil A')
if idade == 8 and idade <=10:
    print('Infantil B')
if idade == 11 and idade <= 13:
    print('Juvenil A')
if idade == 14 and idade <= 17:
    print('Juvenil B')
if idade >= 18:
    print('Adulto')