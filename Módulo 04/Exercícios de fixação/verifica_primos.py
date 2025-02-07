n = int(input("Digite um número inteiro: "))

if n > 1:  
    i = 2
    while i < n:
        if n % i == 0:
            print("não primo")
            break
        i += 1
    else:
        print("primo")
else:
    print("não primo")
