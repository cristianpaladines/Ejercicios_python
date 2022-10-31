pesos = input("¿cual moneda deseas convertir? (dolar o pesos colombianos): ")
if pesos =="pesos colombianos":
    pesos= input("¿cuantos pesos colombianos tienes?: ")

pesos = float(pesos)
valor_dolar = 4835
dolares = pesos / valor_dolar
dolares = round(dolares, 3)
dolares = str(dolares)
print("tienes $" + dolares + " dolares")