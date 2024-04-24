def tabuada_multiplicacao(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Inicia o loop principal
while True:
    # Solicita ao usuário que insira um número de 1 a 9
    numero = int(input("Entre com um número de 1 a 9: "))

    # Verifica se o número está no intervalo correto
    if numero < 1 or numero > 9:
        print("Número inválido. Por favor, entre com um número de 1 a 9.")
        continue

    # Mostra a tabuada de multiplicação do número
    tabuada_multiplicacao(numero)

    # Pergunta ao usuário se deseja calcular outro número
    opcao = input("Calcular outro número (s/n)? ").lower()
    if opcao != 's':
        break
