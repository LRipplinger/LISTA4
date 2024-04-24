# Função para calcular o fatorial de um número
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Inicia o loop principal
while True:
    # Solicita ao usuário que insira um número
    numero = int(input("Entre com um número: "))

    # Calcula o fatorial do número
    resultado = calcular_fatorial(numero)

    # Exibe o resultado
    print(f"O fatorial de {numero} é {resultado}")

    # Pergunta ao usuário se deseja calcular outro número
    opcao = input("Calcular outro número (s/n)? ").lower()
    if opcao != 's':
        break
