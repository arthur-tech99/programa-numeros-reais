ct = 0
soma = 0
maior_que_20 = 0

print("Digite valores reais. Digite -1 para sair.")

while True:
    numero = float(input("Digite um número: "))

    if numero == -1:
        break

    ct += 1
    soma += numero

    if numero > 20:
        maior_que_20 += 1


if ct > 0:
    media = soma / ct
    print("Resultados:")
    print("Quantidade de valores digitados:", ct)
    print("Soma dos valores:", soma)
    print("Média aritmética:", media)
    print("Quantidade de valores maiores que 20:", maior_que_20)
else:
    print("Nenhum número válido foi digitado.")