# Solicita ao usuário que insira o número de linhas
n = int(input("Entre com um número: "))

# Solicita ao usuário que insira o caractere desejado
caractere = input("Entre com um caractere: ")

# Loop para imprimir as linhas
for i in range(1, n + 1):
    print(caractere * i)
