# Ejercicio 1 - Caja del Kiosco

# Validamos que el nombre no esté vacío y tenga solo letras.
cliente = input("Nombre del cliente: ").strip()
while not cliente.isalpha():
    print("Error: el nombre debe tener solo letras.")
    cliente = input("Nombre del cliente: ").strip()

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese una cantidad entera mayor a cero.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)
total_sin_descuento = 0
total_con_descuento = 0.0

# Repetimos una vez por cada producto.
for numero in range(1, cantidad + 1):
    precio = input(f"Producto {numero} - Precio: $")
    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {numero} - Precio: $")

    descuento = input("¿Tiene descuento? (S/N): ").lower()
    while descuento != "s" and descuento != "n":
        print("Error: responda S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    precio = int(precio)
    total_sin_descuento = total_sin_descuento + precio
    if descuento == "s":
        total_con_descuento = total_con_descuento + precio * 0.90
    else:
        total_con_descuento = total_con_descuento + precio

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad
print("\n--- RESUMEN DE COMPRA ---")
print(f"Cliente: {cliente}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
