segundos = int(input("Por favor entre com o número de segundos que deseja converter: "))

a = segundos // 86400

resto = segundos % 86400

b = resto // 3600

resto %= 3600

c = resto // 60

d = resto % 60

print(f"{a} dias, {b} horas, {c} minutos e {d} segundos.")
