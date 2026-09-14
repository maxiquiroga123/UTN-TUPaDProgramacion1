# Ejercicio 4 - Escape Room: La Bóveda
agente = input("Nombre del agente: ").strip()
while not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ").strip()

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# El juego continúa mientras haya recursos y la alarma no haya bloqueado todo.
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(f"\nAgente {agente} | Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: elija una opción del 1 al 3.")
        opcion = input("Opción: ")

    if opcion == "1":
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        # La tercera vez seguida activa la alarma y no abre la cerradura.
        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabó por forzarla tres veces. ¡Alarma activada!")
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese un número del 1 al 3.")
                    riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")
                if riesgo == "3":
                    alarma = True
                    print("¡Alarma activada!")
            if alarma == False:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

    elif opcion == "2":
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        # El for muestra los cuatro pasos del hackeo y completa el código.
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Hackeo paso {paso}/4. Código: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("Código completo: abriste una cerradura.")

    else:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma == True:
            energia -= 10
            print("La alarma te quitó 10 de energía extra.")
        print("Descansaste y recuperaste energía.")

    # Esta regla se revisa después de cada acción.
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("La alarma bloqueó la bóveda por falta de tiempo.")
        break

if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la bóveda.")
elif alarma == True:
    print("DERROTA: el sistema quedó bloqueado por la alarma.")
else:
    print("DERROTA: te quedaste sin energía o sin tiempo.")
