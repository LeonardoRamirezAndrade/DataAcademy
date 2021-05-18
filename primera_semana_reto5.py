#Reto 5 - Rangos cambiantes
#Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.

#Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

#En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número para repetir el proceso

#No entiendo mucho el reto 5 para mi es colocar el numero mayor, por favor acepto feedback

numero1 = int(input('Coloca un numero: '))
numero2 = int(input('Coloca otro numero: '))
numero3 = int(input('Coloca otro numero mas: '))

if numero1 > numero2 and numero3:
    print('Numero1 es el numero mayor')
    if numero2 > numero3:
        print('Numero2 es el segundo mayor')
    else:
        print('Numero3 es el segundo mayor')
elif numero1 == numero2 and numero3:
    print('Los tres numeros son iguales')
elif numero1 == numero2:
    if numero1 > numero3:
        print('Los numeros 1  y 2 son los mayores seguidos del numero 3')
    else:
        print('El numero 3 es el mayor seguido de los numeros 1 y 2')
elif numero1 == numero3:
    if numero1 > numero2:
        print('Los numeros 1  y 3 son los mayores seguidos del numero 2')
    else:
        print('El numero 2 es el mayor seguido de los numeros 1 y 3')
elif numero2 == numero3:
    if numero2 > numero1:
        print('Los numeros 2  y 3 son los mayores seguidos del numero 1')
    else:
        print('El numero 1 es el mayor seguido de los numeros 2 y 3')
elif numero2 > numero1 and numero3:
    print('Numero2 es el numero mayor')
    if numero1 > numero3:
        print('Numero2 es el segundo mayor')
    else:
        print('Numero3 es el segundo mayor')
elif numero3 > numero2 and numero1:
    print('Numero3 es el numero mayor')
    if numero1 > numero2:
        print('Numero2 es el segundo mayor')
    else:
        print('Numero3 es el segundo mayor')
