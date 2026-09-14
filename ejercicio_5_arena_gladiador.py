# Ejercicio 5 - Escape Room: La Arena del Gladiador
nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")
while juego_activo == True and vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador == True:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: ingrese un número válido del 1 al 3.")
            opcion = input("Opción: ")

        if opcion == "1":
            # Si el enemigo está débil, el daño pasa a ser float por el crítico.
            danio_final = danio_pesado
            if vida_enemigo < 20:
                danio_final = danio_pesado * 1.5
                print("¡Golpe crítico!")
            vida_enemigo -= danio_final
            print(f"¡Atacaste al enemigo por {danio_final:.1f} puntos de daño!")

        elif opcion == "2":
            print("¡Inicias una ráfaga de golpes!")
            # La ráfaga conecta tres golpes de cinco puntos cada uno.
            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
                if vida_enemigo <= 0:
                    break
        else:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Usaste una poción y recuperaste 30 de vida.")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    # El enemigo responde solamente si continúa con vida.
    if turno_gladiador == False and vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        turno_gladiador = True

    if vida_jugador <= 0 or vida_enemigo <= 0:
        juego_activo = False

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

