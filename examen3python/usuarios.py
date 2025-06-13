import sys

# Lista para almacenar los usuarios que se van creando
usuarios_creados = []

# Recorre los argumentos pasados al script (excepto el primero, que es el nombre del script)
for argumento in range(1, len(sys.argv)):
    # Si el argumento es '-u', significa que el siguiente argumento será el nombre del usuario a crear
    if sys.argv[argumento] == '-u':
        usuario_ya_creado = False  # Esta variable indica si el usuario ya existe en la lista
        # Si está en False, significa que aún no se ha encontrado el usuario en la lista
        nombre_usuario = sys.argv[argumento + 1]
        for usuario_existente in usuarios_creados:
            if usuario_existente == nombre_usuario:
                usuario_ya_creado = True  # Si se encuentra el usuario, se pone a True
        # Si usuario_ya_creado sigue en False, significa que el usuario no existe y se puede crear
        if not usuario_ya_creado:
            usuarios_creados.append(nombre_usuario)
            print(f"Creando usuario {nombre_usuario}")
        else:
            print(f"Usuario {nombre_usuario} ya ha sido creado")
# En resumen: usuario_ya_creado a False significa que el usuario NO existe aún en la lista, por lo que se puede crear.
# Si se encuentra en la lista, se pone a True y no se crea de nuevo.
