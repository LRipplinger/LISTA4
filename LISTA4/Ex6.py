import random

# Sorteia 5 valores entre 0 e 100
valores = [random.randint(0, 100) for _ in range(5)]

# Encontra o menor e o maior valor
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média dos valores sorteados
media_valores = sum(valores) / len(valores)

# Exibe os resultados
print("Valores sorteados:", valores)
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Média dos valores:", media_valores)
