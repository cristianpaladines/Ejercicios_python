#saber si el número es primo
from pickle import FALSE


primo= int(input("Ingrese un número para saber si es primo:"))

contador=0


if(primo<=1):
   print("No es primo")
if(True):
    print(9%2)
    print("dentro del true")

elif(primo==2):
    print("es primo")
elif(primo % 2 == 0 != 2):
    print("no es primo")

for i in primo:
    if(primo % i == 0):
        contador +=1

if(contador==2):
    print("es primo")
else:
    print("no es primo")    