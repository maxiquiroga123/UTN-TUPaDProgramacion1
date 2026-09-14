# Ejercicio 3 - Agenda de turnos (sin listas ni diccionarios)
operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ").strip()

# Cada variable representa un turno. El texto vacío significa que está libre.
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""
opcion = ""

while opcion != "5":
    print("\n1 Reservar | 2 Cancelar | 3 Ver agenda | 4 Resumen | 5 Salir")
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: ingrese un número del 1 al 5.")
        opcion = input("Opción: ")

    if opcion == "1" or opcion == "2" or opcion == "3":
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: elija 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

    if opcion == "1":
        paciente = input("Nombre del paciente: ").strip()
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente: ").strip()
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Ese paciente ya tiene turno el lunes.")
            elif lunes1 == "": lunes1 = paciente; print("Turno reservado.")
            elif lunes2 == "": lunes2 = paciente; print("Turno reservado.")
            elif lunes3 == "": lunes3 = paciente; print("Turno reservado.")
            elif lunes4 == "": lunes4 = paciente; print("Turno reservado.")
            else: print("No hay turnos libres el lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Ese paciente ya tiene turno el martes.")
            elif martes1 == "": martes1 = paciente; print("Turno reservado.")
            elif martes2 == "": martes2 = paciente; print("Turno reservado.")
            elif martes3 == "": martes3 = paciente; print("Turno reservado.")
            else: print("No hay turnos libres el martes.")

    elif opcion == "2":
        paciente = input("Nombre del paciente a cancelar: ").strip()
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()
        # Si encontramos el nombre, vaciamos esa variable para liberar el turno.
        if dia == "1":
            if paciente == lunes1: lunes1 = ""; print("Turno cancelado.")
            elif paciente == lunes2: lunes2 = ""; print("Turno cancelado.")
            elif paciente == lunes3: lunes3 = ""; print("Turno cancelado.")
            elif paciente == lunes4: lunes4 = ""; print("Turno cancelado.")
            else: print("El paciente no tiene turno el lunes.")
        else:
            if paciente == martes1: martes1 = ""; print("Turno cancelado.")
            elif paciente == martes2: martes2 = ""; print("Turno cancelado.")
            elif paciente == martes3: martes3 = ""; print("Turno cancelado.")
            else: print("El paciente no tiene turno el martes.")

    elif opcion == "3":
        if dia == "1":
            print("Lunes - T1:", lunes1 or "(libre)", "| T2:", lunes2 or "(libre)")
            print("T3:", lunes3 or "(libre)", "| T4:", lunes4 or "(libre)")
        else:
            print("Martes - T1:", martes1 or "(libre)", "| T2:", martes2 or "(libre)")
            print("T3:", martes3 or "(libre)")

    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres.")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres.")
        if ocupados_lunes > ocupados_martes: print("El lunes tiene más turnos.")
        elif ocupados_martes > ocupados_lunes: print("El martes tiene más turnos.")
        else: print("Hay empate entre los dos días.")

    else:
        print("Sistema cerrado. Hasta luego,", operador + ".")
