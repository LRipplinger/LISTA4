import random

# Sorteia um número de 1 a 10
numero_secreto = random.randint(1, 10)

# Inicializa o contador de tentativas
tentativas_restantes = 3

# Inicia o loop para as tentativas
while tentativas_restantes > 0:
    # Solicita ao usuário que faça uma tentativa
    tentativa = int(input("Tente adivinhar o número (entre 1 e 10): "))
    
    # Verifica se a tentativa está correta
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        break
    elif tentativa < numero_secreto:
        print("O número a adivinhar está acima.")
    else:
        print("O número a adivinhar está abaixo.")

    # Decrementa o contador de tentativas restantes
    tentativas_restantes -= 1

# Se as tentativas acabarem, inform
