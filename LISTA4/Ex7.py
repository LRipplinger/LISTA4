# Solicita ao usuário que insira cinco nomes
nomes = [input("Digite um nome: ") for _ in range(5)]

# Encontra o primeiro nome em ordem alfabética
primeiro_nome = min(nomes)

# Exibe o primeiro nome em ordem alfabética
print("O primeiro nome em ordem alfabética é:", primeiro_nome)
