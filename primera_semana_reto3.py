#Reto 3 - Conversor de millas a kilómetros
#Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. Para no estar repitiendo este cálculo escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.

#Toma en cuenta que en cada milla hay 1.609344 Km

#Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.

elección = int(input('Quieres transformar de kilómetros a millas (opción 1) o de millas a kilómetros (opción 2), escribe 1 si deseas la opción 1 y escribe 2 si deseas la opción 2: '))

if elección == 1:
    print('Escogiste de Kilómetros a millas')
    ejercicio = int(input('Coloca los kilómetros que quieres convertir: '))
    solución = ejercicio / 1.609344
    imprimir = print(f'El resultado es {solución} millas')
elif elección == 2:
    print('Escogiste de millas a kilometros')
    ejercicio = int(input('Coloca las millas que quieres convertir: '))
    solución = ejercicio * 1.609344
    imprimir = print(f'El resultado es {solución} kilometros')

