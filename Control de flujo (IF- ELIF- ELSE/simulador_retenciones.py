salario_bruto = float(input("Ingrese el salario bruto: "))
retencion = 0

if salario_bruto <= 1500000:
    print("No paga impuesto a las ganancias")
elif salario_bruto > 1500000 and salario_bruto <= 2500000:
    excedente = salario_bruto - 1500000
    retencion = excedente * 0.15
elif salario_bruto > 2500000:
    excedente = salario_bruto - 2500000
    retencion = excedente * 0.35

print(f"Tu salario neto es {salario_bruto - retencion}")
