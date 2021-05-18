#Retos de Data Academy semana 1
#Reto 1 - Área de un triángulo
#Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

#Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.

#Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno.
b = float(input('Cuál es la base del triangulo ?: '))

h = float(input('Cuál es la altura del triangulo ?: '))

area = (b * h)/2

print(f'El area del triangulo es: {area} cm**2' )

bonus = input('Quieres continuar y saber si tu triangulo es isósceles, equilátero o escaleno.?, si es así responde Y o N: ')

resultado = bonus.upper()

def angulos():
    angulo1 = int(input('Escribe el primer angulo de tu triangulo: '))
    angulo2 = int(input('Escribe el segundo angulo de tu triangulo: '))
    if resultado == 'Y':
        if angulo1 & angulo2 == 60:
            print('Es un triangulo equilatero')
        elif angulo1 == angulo2:
            print('Es un triangulo isoceles')
        elif angulo1 or angulo2 > 178:
            print('Este no es un triangulo por tener datos incorrectos')
        else:
            print('Es un triangulo escaleno')            
    else:
        print('Ok, Gracias por usar la aplicación :) ')


if __name__ == '__main__':
    angulos()