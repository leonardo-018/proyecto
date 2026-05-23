from tkinter import *

# nuetra clase producto
class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad_vendida):

        global ventas_dia

        if cantidad_vendida <= self.cantidad:

            self.cantidad -= cantidad_vendida

            total = cantidad_vendida * self.precio

            ventas_dia += total

            cuadro_texto.insert(END, "\n------ TICKET ------\n")
            cuadro_texto.insert(END, f"Producto: {self.nombre}\n")
            cuadro_texto.insert(END, f"Cantidad: {cantidad_vendida}\n")
            cuadro_texto.insert(END, f"Total: ${total}\n")
            cuadro_texto.insert(END, "Venta correcta\n")
            cuadro_texto.insert(END, "--------------------\n")

            if self.cantidad <= 5:
                cuadro_texto.insert(END, "Queda poquito producto\n")

        else:
            cuadro_texto.insert(END, "No hay suficiente producto\n")


#nuestras variabakes a usar

inventario = []
ventas_dia = 0

# funciones que vamos a usar

def agregar_producto():

    nombre = entrada_nombre.get()
    precio = float(entrada_precio.get())
    cantidad = int(entrada_cantidad.get())
    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)
    cuadro_texto.insert(END, f"\nSe agrego: {nombre}")
    cuadro_texto.insert(END, f"\nPrecio: {precio}")
    cuadro_texto.insert(END, f"\nCantidad: {cantidad}")

def mostrar_inventario():

    cuadro_texto.insert(END, "\n===== INVENTARIO =====\n")
    if len(inventario) == 0:
        cuadro_texto.insert(END, "Inventario vacío\n")
    else:
        for producto in inventario:
            cuadro_texto.insert(
                END,
                f"{producto.nombre} | "
                f"${producto.precio} | "
                f"Cantidad: {producto.cantidad}\n"
            )


def buscar_producto():

    nombre = entrada_buscar.get()
    for producto in inventario:
        if producto.nombre.lower() == nombre.lower():
            cuadro_texto.insert(END, "\nProducto encontrado\n")
            cuadro_texto.insert(
                END,
                f"{producto.nombre} | "
                f"${producto.precio} | "
                f"Cantidad: {producto.cantidad}\n"
            )

            return

    cuadro_texto.insert(END, "\nProducto no encontrado\n")


def vender_producto():

    nombre = entrada_buscar.get()
    cantidad = int(entrada_vender.get())

    for producto in inventario:

        if producto.nombre.lower() == nombre.lower():
            producto.vender(cantidad)
            return

    cuadro_texto.insert(END, "\nProducto no encontrado\n")


def mostrar_ventas():

    cuadro_texto.insert(
        END,
        f"\nTotal vendido del día: ${ventas_dia}\n"
    )


# la ventana que vamos a llamar tiendita

ventana = Tk()

ventana.title("Tiendita")
ventana.geometry("600x600")

# entradas donde podemos introducir datos


Label(ventana, text="Nombre").pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()

Label(ventana, text="Precio").pack()
entrada_precio = Entry(ventana)
entrada_precio.pack()

Label(ventana, text="Cantidad").pack()
entrada_cantidad = Entry(ventana)
entrada_cantidad.pack()

Label(ventana, text="Buscar / vender producto").pack()
entrada_buscar = Entry(ventana)
entrada_buscar.pack()

Label(ventana, text="Cantidad a vender").pack()
entrada_vender = Entry(ventana)
entrada_vender.pack()

# botones de la ventana

Button(
    ventana,
    text="Agregar producto",
    command=agregar_producto
).pack()

Button(
    ventana,
    text="Mostrar inventario",
    command=mostrar_inventario
).pack()

Button(
    ventana,
    text="Buscar producto",
    command=buscar_producto
).pack()

Button(
    ventana,
    text="Vender producto",
    command=vender_producto
).pack()

Button(
    ventana,
    text="Mostrar ventas",
    command=mostrar_ventas
).pack()

# cuadro de texto

cuadro_texto = Text(ventana, height=20, width=60)
cuadro_texto.pack()

# ejecutamos
ventana.mainloop()
