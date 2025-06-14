# Juego de Aventura de Decisiones
# El usuario toma decisiones y acumula puntos según sus elecciones

puntos = 0  # Variable para llevar la cuenta de los puntos

# Primera decisión: elegir puerta
print("Estás en una habitación misteriosa con dos puertas: una roja y una verde.")
puerta = input("¿Qué puerta eliges? (roja/verde): ").strip().lower()

if puerta == "verde":
    puntos += 20
    print("Has elegido la puerta verde. Ganas 20 puntos y llegas a un bosque con un río.")
    # Segunda decisión en el bosque
    decision_bosque = input("¿Quieres adentrarte en el bosque o coger una lancha en el río? (bosque/lancha): ").strip().lower()
    if decision_bosque == "bosque":
        puntos -= 10
        print("Te adentras en el bosque. Pierdes 10 puntos y termina el juego.")
        print(f"Puntos finales: {puntos}")
    elif decision_bosque == "lancha":
        puntos += 20
        print("Coges una lancha y bajas por el río. Ganas 20 puntos.")
        # Tercera decisión en la bifurcación
        direccion = input("Llegas a una bifurcación. ¿Tomas la derecha o la izquierda? (derecha/izquierda): ").strip().lower()
        if direccion == "derecha":
            puntos -= 10
            print("Te caes por una cascada. Pierdes 10 puntos y termina el juego.")
            print(f"Puntos finales: {puntos}")
        elif direccion == "izquierda":
            puntos += 30
            print("Llegas a un museo y ganas 30 puntos.")
            # Cuarta decisión en el museo
            sala = input("¿Quieres ir a la sala de la momia o salir del museo? (momia/salir): ").strip().lower()
            if sala == "momia":
                puntos -= 10
                print("La momia se levanta. Pierdes 10 puntos y termina el juego.")
                print(f"Puntos finales: {puntos}")
            elif sala == "salir":
                print("Encuentras un taxi al salir del museo.")
                # Quinta decisión: taxi
                taxi = input("¿Quieres coger el taxi? (si/no): ").strip().lower()
                if taxi == "si":
                    puntos += 20
                    print("Coges el taxi. Ganas 20 puntos y termina el juego.")
                    print(f"Puntos finales: {puntos}")
                else:
                    puntos -= 10
                    print("Te cae un rayo. Pierdes 10 puntos y termina el juego.")
                    print(f"Puntos finales: {puntos}")
        else:
            print("Opción no válida. El juego termina.")
            print(f"Puntos finales: {puntos}")
    else:
        print("Opción no válida. El juego termina.")
        print(f"Puntos finales: {puntos}")
elif puerta == "roja":
    puntos += 10
    print("Has elegido la puerta roja. Ganas 10 puntos y entras en un museo.")
    # Cuarta decisión en el museo
    sala = input("¿Quieres ir a la sala de la momia o salir del museo? (momia/salir): ").strip().lower()
    if sala == "momia":
        puntos -= 10
        print("La momia se levanta. Pierdes 10 puntos y termina el juego.")
        print(f"Puntos finales: {puntos}")
    elif sala == "salir":
        print("Encuentras un taxi al salir del museo.")
        # Quinta decisión: taxi
        taxi = input("¿Quieres coger el taxi? (si/no): ").strip().lower()
        if taxi == "si":
            puntos += 20
            print("Coges el taxi. Ganas 20 puntos y termina el juego.")
            print(f"Puntos finales: {puntos}")
        else:
            puntos -= 10
            print("Te cae un rayo. Pierdes 10 puntos y termina el juego.")
            print(f"Puntos finales: {puntos}")
    else:
        print("Opción no válida. El juego termina.")
        print(f"Puntos finales: {puntos}")
else:
    print("Opción no válida. El juego termina.")
    print(f"Puntos finales: {puntos}")

# Explicación:
# - Se usan variables descriptivas para cada decisión.
# - Se suman o restan puntos según las elecciones.
# - El juego termina en cada rama según las reglas del enunciado.
# - Se muestra el puntaje final al terminar la aventura.
