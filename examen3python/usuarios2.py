import sys

# Lista para guardar los nombres de los usuarios creados
lista_usuarios = []
# Lista para contar cuántas veces se repite cada usuario
lista_repeticiones = []

# Explicación:
# - lista_usuarios guarda los nombres únicos de usuarios.
# - lista_repeticiones lleva la cuenta de cuántas veces se repite cada usuario.
# - Si el usuario es nuevo, se agrega a ambas listas y se imprime su nombre.
# - Si ya existe, se incrementa su contador y se imprime el nombre con el número correspondiente.

# Recorremos los argumentos recibidos por el script
for indice in range(1, len(sys.argv)):
    # Si el argumento es '-u', el siguiente argumento es el nombre del usuario
    if sys.argv[indice] == '-u':
        usuario_nuevo = True  # Suponemos que el usuario es nuevo
        nombre_usuario = sys.argv[indice + 1]
        # Buscamos si el usuario ya está en la lista
        for posicion in range(len(lista_usuarios)):
            if lista_usuarios[posicion] == nombre_usuario:
                usuario_nuevo = False  # Si lo encontramos, ya no es nuevo
        if usuario_nuevo:
            lista_usuarios.append(nombre_usuario)
            print(f"Creando usuario {nombre_usuario}")
            lista_repeticiones.append(0)  # Primera vez, contador en 0
        else:
            # Si ya existe, aumentamos el contador y mostramos el nombre con el número
            posicion_usuario = lista_usuarios.index(nombre_usuario)
            lista_repeticiones[posicion_usuario] += 1
            print(f"Creando usuario {nombre_usuario}{lista_repeticiones[posicion_usuario]}")
