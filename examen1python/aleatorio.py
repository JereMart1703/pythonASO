# Juego de adivinar el número aleatorio entre 1 y 100
# El usuario debe adivinar el número y se otorgan puntos según la cercanía
import random

puntos = 0  # Puntos acumulados
numero_aleatorio = random.randint(1, 100)  # Número que el programa "piensa"
juego_activo = True

while juego_activo:
    intento = int(input("¿Cuál crees que es el número (entre 1 y 100)?: "))
    diferencia = abs(numero_aleatorio - intento)
    # Si la diferencia es mayor o igual a 30, pierdes y tienes 0 puntos
    if diferencia >= 30:
        print("Has perdido")
        puntos = 0
        juego_activo = False
    # Si la diferencia es menor de 5, ganas 40 puntos y termina
    elif diferencia < 5:
        puntos += 40
        print(f"¡Muy cerca! Has ganado. Puntos totales: {puntos}")
        juego_activo = False
    # Si la diferencia es menor de 20, sumas 30 puntos y sigues jugando
    elif diferencia < 20:
        puntos += 30
        print(f"Estás bastante cerca. Puntos actuales: {puntos}")
        numero_aleatorio = random.randint(1, 100)  # Nuevo número para seguir jugando
    # Si la diferencia es menor de 30 pero mayor o igual a 20, pierdes y termina
    elif diferencia < 30 and diferencia >= 20:
        print(f"Has perdido. Puntos totales: {puntos}")
        juego_activo = False
    # Si la diferencia es menor de 30 pero mayor o igual a 10, sumas 10 puntos y sigues jugando
    elif diferencia < 30 and diferencia >= 10:
        puntos += 10
        print(f"Estás cerca. Puntos actuales: {puntos}")
        numero_aleatorio = random.randint(1, 100)

# Explicación:
# - El programa genera un número aleatorio y pregunta al usuario.
# - Según la diferencia, suma puntos o termina el juego.
# - No se usan 'continue', solo se controla el flujo con 'if-elif-else' y una variable booleana.
