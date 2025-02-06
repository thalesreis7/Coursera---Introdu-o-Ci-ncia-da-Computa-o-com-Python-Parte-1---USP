import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

d = b ** 2 - 4 * a * c

if d == 0:
    raiz_01 = (-b + math.sqrt(d)) / (2 * a)
    print(f"a raiz desta equação é {raiz_01}")
else:
    if d < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz_01 = (-b + math.sqrt(d)) / (2 * a)
        raiz_02 = (-b + math.sqrt(d)) / (2 * a)
        print("as raízes da equação são ", (raiz_01, raiz_02))
