# Ejercicio 2 - Acceso al Campus y Menú Seguro
usuario_correcto = "alumno"
clave_correcta = "python123"
intento = 1
acceso_concedido = False

# El usuario dispone de hasta tres intentos para ingresar.
while intento <= 3 and acceso_concedido == False:
    usuario = input(f"Intento {intento}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")
        intento = intento + 1

if acceso_concedido == False:
    print("Cuenta bloqueada.")
else:
    opcion = ""
    # El menú continúa hasta que se elige la opción 4.
    while opcion != "4":
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: ingrese una opción numérica del 1 al 4.")
            opcion = input("Opción: ")

        if opcion == "1":
            print("Estado de inscripción: Inscripto.")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirmacion = input("Confirmar nueva clave: ")
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar nueva clave: ")
            clave_correcta = nueva_clave
            print("Clave actualizada correctamente.")
        elif opcion == "3":
            print("¡Seguí practicando, cada ejercicio suma experiencia!")
        else:
            print("Sesión finalizada.")
