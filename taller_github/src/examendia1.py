productos = int(input("Cuantos articulos deseas agregar: "))
nombres = []
precios = []
cantidades = []
semaforo = True
while semaforo:

    nombres.append(input("Ingresa el nombre: "))
    precios.append(float(input("Ingresa el precio: ")))
    cantidades.append(int(input("Ingresa la cantidad: ")))

    if len(nombres) == productos:
        semaforo = False

for indice, valor in enumerate(nombres):
    print(
        f"Producto: {nombres[indice]}, Precio: {precios[indice]}, Cantidad: {cantidades[indice]}"
    )

print(f"Valor total del inventario: {sum(precios)}")

buscar = input("Desas buscar un producto por su nombre? (si/no)")

if buscar.lower() == "si":
    nombre = input("Ingresa el nombre del producto: ")
    for indice, valor in enumerate(nombres):
        if nombre.lower() == valor.lower():
            print(
                f"Nombre: {nombres[indice]}, Precio: {precios[indice]}, Cantidad: {cantidades[indice]}"
            )
            break
    else:
        print("Producto no encontrado")

buscar = input("Desas eliminar un producto por su nombre? (si/no)")

if buscar.lower() == "si":
    nombre = input("Ingresa el nombre del producto: ")
    for indice, valor in enumerate(nombres):
        if nombre.lower() == valor.lower():
            del nombres[indice]
            del precios[indice]
            del cantidades[indice]
            print(f"Producto eliminado: {nombre}")
            break
    else:
        print("Producto no encontrado")

print("Inventario actualizado:")
for indice, valor in enumerate(nombres):
    print(
        f"Producto: {nombres[indice]}, Precio: {precios[indice]}, Cantidad: {cantidades[indice]}"
    )

print(f"Valor actualizado del inventario: {sum(precios)}")
