# Programa para registrar temperaturas y calcular la media descartando valores fuera del rango 35-40ºC
# Autor: (tu nombre)

# Variables descriptivas
lista_descartadas = ""  # Guarda las temperaturas descartadas como texto
suma_temperaturas = 0.0  # Suma de temperaturas válidas
total_personas = 1       # Contador total de personas
personas_validas = 0     # Contador de personas con temperatura válida
respuesta_usuario = "si"  # Respuesta para continuar

while respuesta_usuario != "no":
    # Pedimos la temperatura de la persona actual
    temperatura_actual = float(input(f"Introduce la temperatura de la persona {total_personas}: "))
    # Preguntamos si quiere introducir más temperaturas
    respuesta_usuario = input("¿Quieres introducir más temperaturas?(sí/no). Por defecto sí. ")
    # Si la temperatura está fuera del rango válido, la descartamos
    if temperatura_actual > 40 or temperatura_actual < 35:
        lista_descartadas += str(temperatura_actual) + ", "
    else:
        suma_temperaturas += temperatura_actual
        personas_validas += 1
    total_personas += 1

# Mostramos el total de personas y las temperaturas descartadas
print(f"Se han medido un total de {total_personas} personas, de las cuales hemos descartado las siguientes temperaturas:")
print(f"{lista_descartadas} (ºC)")
# Calculamos y mostramos la media de las temperaturas válidas
if personas_validas > 0:
    media = suma_temperaturas / personas_validas
    print(f"Es decir que la temperatura media es de {media:.2f} (ºC) para las {personas_validas} personas")
else:
    print("No hay temperaturas válidas para calcular la media.")

# Notas explicativas:
# - lista_descartadas: almacena las temperaturas fuera del rango 35-40ºC.
# - suma_temperaturas: suma solo las temperaturas válidas.
# - total_personas: cuenta todas las personas introducidas.
# - personas_validas: cuenta solo las personas con temperatura válida.
# - El bucle pregunta por más temperaturas hasta que se responde 'no'.
# - Al final, se muestra la media solo si hay temperaturas válidas.
