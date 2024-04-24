import random

# Gerar e escrever todos os números inteiros do intervalo [0,100]
print("Todos os números inteiros do intervalo [0,100]:")
for i in range(101):
    print(i, end=' ')
print("\n")

# Gerar e escrever os números pares do intervalo [20,50]
print("Números pares do intervalo [20,50]:")
for i in range(20, 51, 2):
    print(i, end=' ')
print("\n")

# Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente
print("Números inteiros do intervalo [25,70] em ordem decrescente:")
for i in range(70, 24, -1):
    print(i, end=' ')
print("\n")

# Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente
print("Números ímpares do intervalo [25,95] em ordem decrescente:")
for i in range(95, 24, -1):
    if i % 2 != 0:
        print(i, end=' ')
print("\n")

# Ler 15 números e escrever a soma e a média dos números lidos
numeros = [float(input("Digite um número: ")) for _ in range(15)]
soma = sum(numeros)
media = soma / 15
print("Soma dos números:", soma)
print("Média dos números:", media)

# Ler 10 números inteiros e escrever a quantidade de números pares e ímpares lidos
numeros_inteiros = [int(input("Digite um número inteiro: ")) for _ in range(10)]
pares = sum(1 for num in numeros_inteiros if num % 2 == 0)
impares = sum(1 for num in numeros_inteiros if num % 2 != 0)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

# Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem
# “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso.
positivos = 0
negativos = 0
print("Números sorteados e suas classificações:")
for _ in range(20):
    num = random.randint(-10, 10)
    if num > 0:
        print(num, "POSITIVO")
        positivos += 1
    elif num < 0:
        print(num, "NEGATIVO")
        negativos += 1
    else:
        print(num, "NULO")
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)

# Ler n números e imprimir no final a soma dos números lidos
n = int(input("Quantos números deseja ler? "))
numeros_lidos = [float(input("Digite um número: ")) for _ in range(n)]
soma = sum(numeros_lidos)
print("A soma dos números lidos é:", soma)
