aprovados = 0
reprovados = 0
total_alunos = 0

while True:
    try:
        nota = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
        if nota.lower() == 'sair':
            break

        nota = float(nota)
        total_alunos += 1

        if nota >= 5.0:
            aprovados += 1
        else:
            reprovados += 1
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

print("Resultados:")
print(f"Total de alunos: {total_alunos}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")