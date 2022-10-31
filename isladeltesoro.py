print("++++++++++++++++++++++++++++++++++++++++")
print("Algoritmo de la isla del tesoro")
print("++++++++++++++++++++++++++++++++++++++++")

print("Bienvenido a la isla del tesoro, tu mision es encontrar el tesoro")
camino = input("Tienes tres caminos ¿cual eliges? (derecha, izquierda o medio)")

if camino =="derecha":
    print("caiste en un agujero GAME OVER (vuelve a empezar)")
elif camino=="medio":
    print("conoces a una tribu amigable y te ayuda a llegar al final y conseguir el tesoro HAZ GANADO")
elif camino=="izquierda":
    nadar_o_escapar = input("tienes dos opciones ¿cual eliges? (nadar o escapar)")
if nadar_o_escapar =="nadar":
    print("te comio un tiburon GAME OVER (vuelve a empezar)")
elif nadar_o_escapar =="escapar":
    cual_puerta = input("te ecuentras con varias puertas ¿cual eliges? (azul, rojo, morado, verde o madera)")
if cual_puerta =="azul":
    print("eres devorado por bestias GAME OVER (vuelve a empezar)")
elif cual_puerta =="rojo":
    print("eres quemado GAME OVER (vuelve a empezar)")
elif cual_puerta =="morado":
    print("quedas encerrado en cuarto lleno de gas toxico GAME OVER (vuelve a empezar)")
elif cual_puerta =="verde":
    print("caes en una trampa que te encierra de por vida GAME OVER (vuelve a empezar)")
elif cual_puerta =="madera":
    print("GANASTE: HAS ENCONTRADO EL TESORO SECRETO")
else:
    print("VALOR NO VALIDO")