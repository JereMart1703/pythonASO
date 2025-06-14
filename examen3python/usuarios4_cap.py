import sys

# Contador de usuarios
cantidad_usuarios = 0
# Suma total de capacidad utilizada
capacidad_total_utilizada = 0.0
# Lista de nombres de usuarios
lista_usuarios = []
# Lista de capacidades de cada usuario
lista_capacidades = []

# Capacidad total del sistema LVM en TB
capacidad_total = 10.0
mostrar_encima_media = False

# Recorremos los argumentos recibidos por el script
indice = 1
while indice < len(sys.argv):
    if sys.argv[indice] == '-u':
        # Sumamos la capacidad de este usuario
        capacidad_total_utilizada += float(sys.argv[indice + 2])
        # Guardamos el nombre y la capacidad
        lista_usuarios.append(sys.argv[indice + 1])
        lista_capacidades.append(float(sys.argv[indice + 2]))
        cantidad_usuarios += 1
        indice += 3
    elif sys.argv[indice] == '-encima_media':
        mostrar_encima_media = True
        indice += 1
    else:
        indice += 1

# Calculamos el porcentaje de ocupación
porcentaje_ocupado = capacidad_total_utilizada / capacidad_total * 100
# Mostramos el resultado principal
print(f"Tenemos {cantidad_usuarios} usuarios, con {capacidad_total_utilizada:.2f} (TB) utilizados de {capacidad_total:.2f} (TB), una ocupación total de ({porcentaje_ocupado:.2f}%)")

# Calculamos la media de capacidad por usuario
media_capacidad = capacidad_total / cantidad_usuarios

# Si se pide mostrar los usuarios por encima de la media
if mostrar_encima_media:
    salida = "Tenemos los usuarios "
    for i in range(len(lista_usuarios)):
        if lista_capacidades[i] > media_capacidad:
            # Mostramos el usuario y cuánto se pasa de la media
            salida += f'{lista_usuarios[i]} con {(lista_capacidades[i] - media_capacidad):.2f}(TB), '
    print(salida + "por encima de la media")

# Explicación:
# - cantidad_usuarios: cuenta cuántos usuarios hay.
# - capacidad_total_utilizada: suma la capacidad de todos los usuarios.
# - lista_usuarios y lista_capacidades: guardan los nombres y capacidades.
# - Se calcula el porcentaje de ocupación y la media.
# - Si se pasa '-encima_media', muestra los usuarios que superan la media y cuánto la superan.
