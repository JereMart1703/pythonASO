import sys

# Capacidad total del sistema LVM en TB
capacidad_total = 10.0
# Lista para guardar los usuarios y sus capacidades
usuarios = []
capacidades = []

# Recorremos los argumentos recibidos por el script
for i in range(1, len(sys.argv)):
    # Si el argumento es '-u', el siguiente es el nombre y el siguiente la capacidad
    if sys.argv[i] == '-u':
        nombre_usuario = sys.argv[i + 1]
        capacidad_usuario = float(sys.argv[i + 2])
        usuarios.append(nombre_usuario)
        capacidades.append(capacidad_usuario)

# Calculamos el total de capacidad utilizada
capacidad_utilizada = sum(capacidades)
# Calculamos el porcentaje de ocupación
porcentaje_ocupacion = (capacidad_utilizada / capacidad_total) * 100

# Mostramos el resultado con el formato solicitado
print(f"Tenemos {len(usuarios)} usuarios, con {capacidad_utilizada:.2f} (TB) utilizados de {capacidad_total:.2f} (TB), una ocupación del ({porcentaje_ocupacion:.2f} %)")

# Explicación:
# - Se recogen los nombres y capacidades de los usuarios desde los argumentos.
# - Se suman las capacidades para obtener el total utilizado.
# - Se calcula el porcentaje respecto a la capacidad total.
# - Se imprime el resultado en el formato pedido.
