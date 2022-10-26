print("++++++++++++++++++++++++++++++++")
print("Algoritmo de la isla del tesoro")
print("++++++++++++++++++++++++++++++++")

print("Bienvenido a la isla. Tu misión será encontrar el tesoro") 

camino=input("hay dos caminos, ¿Cual camino eliges (derecha, izquierda o medio)? :")
 
if camino=="derecha":
    print("Caíste en Agujero 'GAME OVER' ")

elif camino=="izquierda":
    nadar_o_no=input("tienes dos opciones nadar o escapar:")
    if nadar_o_no =="nadar":
        print("Te comio un tiburon 'GAME OVER'")
    elif nadar_o_no=="escapar":
        print("te encuentras cuatro puertas, ¿cual eliges: (azul, roja, verde, morada y madera)?")
        puertas=input("¿Cual puerta? (azul, roja, verde, morado y madera) :")
        if puertas=="azul":
            print("Devorado por bestias 'GAME OVER' ")
        elif puertas=="morado": 
            print("cuarto con gas toxico adentro 'GAME OVER' ")
        elif puertas=="verde":
            print("Una trampa que te atrapa de por vida 'GAME OVER' ")
        elif puertas=="roja" or puertas=="rojo":
            print("Eres quemado 'GAME OVER' ")
        elif puertas=="madera":
            print("Haz ganado")
        else:
            print("ERROR NO SE RECONOCE")    
            

    else:
        print("La opcion no esta disponible") 

elif camino=="medio":
    print("Conoces a una tribu amigable y te ayuda a llegar al final")
else:
    print("Lo sentimos la opcion escogida no esta disponible.")

    

