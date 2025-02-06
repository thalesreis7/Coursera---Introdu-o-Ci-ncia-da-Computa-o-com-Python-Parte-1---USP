nome_do_cliente = input("Digite seu nome: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor_fatura = input("Digite o valor da fatura: ")

if "." in valor_fatura:
    valor_fatura =  (valor_fatura.replace(',', '.'))
    valor_fatura = valor_fatura.replace(',', '|').replace('.', ',').replace('|', '.') 
else:
    valor_fatura = valor_fatura + ',00'
    
print(f"Olá, {nome_do_cliente}\nA fatura com vencimento em {dia_vencimento} de {mes_vencimento} no valor de R${valor_fatura} está fechado")