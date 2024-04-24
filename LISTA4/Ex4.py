# Solicita ao usuário o valor do divisor
divisor = int(input("Entre com o valor do divisor: "))

# Solicita ao usuário o valor inicial e final do intervalo
inicio_intervalo = int(input("Início do intervalo: "))
final_intervalo = int(input("Final do intervalo: "))

# Inicializa uma lista para armazenar os números divisíveis pelo divisor
divisiveis = []

# Loop através do intervalo especificado pelo usuário para encontrar os números divisíveis
for numero in range(inicio_intervalo, final_intervalo + 1):
    if numero % divisor == 0:
        divisiveis.append(numero)

# Exibe os números divisíveis encontrados
print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {final_intervalo}:")
for numero in divisiveis:
    print(numero, end=" ")
