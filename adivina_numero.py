import random

#aqui vamos a trabajar en la linea de cabecera
# a la par se agrega una linea en master
def run():
    numero_aleatorio = random.randint(1,100)
    print ("vas a tener 5 intentos para adivinar el numero")
    numero_elegido = int(input("elige un numero del 1 al 100: "))

    contador = 1
    while contador <5:
        if numero_elegido < numero_aleatorio:
            print ('busca un numero más grande')
            numero_elegido =int(input('elige otro numero: '))

        elif numero_elegido > numero_aleatorio:
            print ('Busca un numero más pequeño')
            numero_elegido =int(input('elige otro numero: '))
        else:
            print ("ganaste")
            contador =5

        contador =contador + 1

    print ("el juego terminó")
   


    
if __name__=='__main__':
    run()
