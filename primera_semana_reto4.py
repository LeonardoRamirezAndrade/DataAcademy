#Reto 4 - Calculadora de volúmenes
#Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.

#Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa recibiendo datos como altura y radio.

#Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.

print('Este es un programa donde puedes saber el volumen de las siguientes figuras: Cilindro, esfera y un cubo')

opción = int(input('Escoges una opción escribiendo el numero: 1 = Cilindro, 2 = esfera y 3 = cubo: '))

if opción == 1:
    h = float(input('Cuál es la altura?: '))
    r = float(input('Cuál es el radio?: '))
    pi = 3.1416
    area_de_la_base = (pi*r**2)
    volumen = area_de_la_base * h
    print(f'El volumen de un cilindro es: {volumen} cm**3 y el area de la base del circulo es: {area_de_la_base} cm**2')
elif opción == 2:
    r = int(input('Cuál es el radio?: '))
    potencia = r**3
    pi = 3.1416
    volumen = (4/3 * pi * potencia)
    print(f'El volumen de una esfera es: {volumen} cm**3 ' )
elif opción == 3:
    lado = int(input('Coloca la base del cubo: '))
    volumen = lado**3
    print(f'El volumen del cubo es: {volumen} cm**3')
