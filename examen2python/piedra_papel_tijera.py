# Script para analizar todas las combinaciones de piedra, papel o tijera entre 3 jugadores
# Autor: (tu nombre)

opciones = ['piedra', 'papel', 'tijera']  # Opciones posibles para cada jugador
empates = 0  # Contador de partidas que terminan en empate
ganadores = 0  # Contador de partidas donde uno o más ganan

# Recorremos todas las combinaciones posibles (3x3x3 = 27)
for jugador1 in opciones:
    for jugador2 in opciones:
        for jugador3 in opciones:
            jugadas = [jugador1, jugador2, jugador3]
            # Caso 1: Todos eligen lo mismo (empate)
            if jugadas.count(jugador1) == 3:
                empates += 1
            # Caso 2: Todos eligen diferente (empate)
            elif len(set(jugadas)) == 3:
                empates += 1
            # Caso 3: Dos eligen lo mismo y uno diferente (hay ganador)
            else:
                ganadores += 1

print(f"Se han analizado las 27 combinaciones de las cuales {empates} se quedan en empate y {ganadores} uno de los jugadores gana")

# Explicación:
# - opciones: lista con las jugadas posibles.
# - empates: cuenta los empates (todos igual o todos diferente).
# - ganadores: cuenta cuando dos eligen igual y uno diferente.
# - Se recorren todas las combinaciones posibles con tres bucles anidados.
# - Se analiza cada caso según las reglas del juego.
