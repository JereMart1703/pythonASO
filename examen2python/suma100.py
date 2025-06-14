# Script para sumar las 100 primeras fracciones de la serie: 4/1 - 4/3 + 4/5 - 4/7 + ...
# Autor: (tu nombre)

suma_total = 0.0  # Acumula la suma de la serie
signo = 1         # Alterna el signo de cada término

# Recorremos los 100 primeros términos
for n in range(100):
    denominador = 1 + 2 * n  # Los denominadores son impares: 1, 3, 5, 7, ...
    termino = 4 / denominador * signo
    suma_total += termino
    signo *= -1  # Cambia el signo para el siguiente término

print(f"La suma de las 100 primeras fracciones es: {suma_total}")

# Explicación:
# - suma_total: almacena el resultado de la suma.
# - signo: alterna entre positivo y negativo para cada término.
# - El bucle genera los denominadores impares y suma/resta cada fracción.
# - Al final, se muestra el resultado de la suma.
