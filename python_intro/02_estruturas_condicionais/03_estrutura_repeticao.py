# Estruturas de repeticao são usadas para executar um bloco de código repetidamente, 
# enquanto uma condição for verdadeira. Em Python, as principais estruturas de repetição são o while e o for.

texto = ""
VOGAIS = "AEIOU"

for letra in VOGAIS:
    if letra.upper() in VOGAIS:
        print(letra,end="")


# range é uma função que gera uma sequência de números, muito útil para criar loops for.
for i in range(5):
    print(i) # Imprime os números de 0 a 4

# exibindo a tabuada do 5 usando for e range
for i in range(1, 11):
    print(f'5 x {i} = {5 * i}')

# while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.
contador = 0
while contador < 5:
    print(contador) # Imprime os números de 0 a 4
    contador += 1


while True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() == 'n':
        print("Encerrando o programa.")
        break
    elif resposta.lower() == 's':
        print("Continuando o programa.")
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")