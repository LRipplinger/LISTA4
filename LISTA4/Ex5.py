# Função para calcular a média de um aluno com base nas notas dos graus A, B e C
def calcular_media(nota_a, nota_b, nota_c):
    media = (nota_a + nota_b) / 2
    if media >= 7:
        return "APROVADO"
    else:
        # Solicita ao usuário qual nota deve ser substituída
        substituir = input("Digite qual nota deve ser substituída (A ou B): ").upper()
        if substituir == 'A':
            media_substituida = (nota_b + nota_c) / 2
        elif substituir == 'B':
            media_substituida = (nota_a + nota_c) / 2
        else:
            print("Opção inválida.")
            return None
        
        if media_substituida >= 7:
            return "APROVADO"
        else:
            return "REPROVADO"

# Inicializa uma lista para armazenar as médias dos alunos
medias_alunos = []

# Solicita ao usuário o número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Loop para ler as notas de cada aluno e calcular a média
for i in range(1, num_alunos + 1):
    print(f"Aluno {i}:")
    nota_a = float(input("Digite a nota do Grau A: "))
    nota_b = float(input("Digite a nota do Grau B: "))
    situacao = calcular_media(nota_a, nota_b, 0)
    if situacao is None:
        break
    elif situacao == "APROVADO":
        print("APROVADO")
    else:
        nota_c = float(input("Digite a nota do Grau C: "))
        situacao = calcular_media(nota_a, nota_b, nota_c)
        print(situacao)
    if situacao is not None:
        medias_alunos.append((nota_a + nota_b) / 2)

# Calcula a média geral dos alunos
media_geral = sum(medias_alunos) / len(medias_alunos)
print("A média geral dos alunos é:", media_geral)
