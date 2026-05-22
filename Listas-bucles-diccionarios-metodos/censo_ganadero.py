stock_vacas = 100
mes = 1

while stock_vacas >= 50:
    mes = mes + 1
    stock_vacas = stock_vacas - 5
    print(f"En el mes {mes} quedan {stock_vacas} vacas en el stock.")
        
print(f"Pasaron {mes} meses y quedan menos de 50 vacas en el stock.")