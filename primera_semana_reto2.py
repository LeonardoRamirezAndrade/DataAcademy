#Reto 2 - Piedra, papel o tijera
#Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.

#Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

#Ejemplo:

#ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2


print('Vamos a jugar piedra papel o tijera :)')

def jugadores():
    jugador1 = int(input('Eres el jugador 1 escribe la opción que quieras con el numero indicado: 1 = piedra, 2 = papel y 3 = tijera: '))
    jugador2 = int(input('Eres el jugador 2 escribe la opción que quieras con el numero indicado: 1 = piedra, 2 = papel y 3 = tijera: '))
    rondas = 1
    if jugador1 == jugador2 :
        print('Empate')
    elif jugador1 == 1 and jugador2 == 2:
        print('Gana el jugador2')
    elif jugador1 == 1 and jugador2 == 3:
        print('Gana el jugador1')
    elif jugador1 == 2 and jugador2 == 3:
        print('Gana el jugador2')
    else:
        print('Escoge una opción correcta ')

if __name__ == '__main__':
    jugadores()