# numero = int(input("Ingresa un número"))
# if numero % 2 == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")

numero=int(input("Ingrese el valor para comprobar"))
list=[x for x in range(2,numero) if numero%==0]
if len(list)!=0:
    print("el número no es primo")
else: 
    print ("el número es primo")