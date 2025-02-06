n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    i = 0
    while i < n:
        print(2 * i + 1)
        i += 1
else:
    print("Número inválido.")

