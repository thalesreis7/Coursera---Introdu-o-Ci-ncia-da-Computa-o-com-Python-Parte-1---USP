nome_do_cliente = input("Digite seu nome: ")
dia_vencimento = input("Digite o dia de vencimento: ")
mes_vencimento = input("Digite o mês de vencimento: ")
valor_fatura = input("Digite o valor da fatura: ")

# Formata o valor da fatura
if "." in valor_fatura:
    # Converte para float e formata com duas casas decimais
    valor_fatura = float(valor_fatura.replace(',', '.'))  # Substitui vírgula por ponto para conversão
    valor_fatura = f"{valor_fatura:,.2f}"  # Formata com separador de milhar (vírgula) e duas casas decimais
    valor_fatura = valor_fatura.replace(',', '|').replace('.', ',').replace('|', '.')  # Ajusta para o padrão desejado
else:
    valor_fatura = valor_fatura + ',00'  # Adiciona ",00" se não houver casas decimais

# Exibe a mensagem final
print(f"Olá, {nome_do_cliente}\nA fatura com vencimento em {dia_vencimento} de {mes_vencimento} no valor de R${valor_fatura} está fechada.")