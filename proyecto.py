class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        print("\n--Producto--")
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def vender(self,cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            total = cantidad_vendida * self.precio
            print("total:", total)
            print("venta correcta")
        else:
            print("no hay suficiente producto")

inventario = []
def agregar():
    nombre = input("Nombre del producto:")
    precio = float(input("precio:"))
    cantidad = int(input("Cantidad:"))

    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)

    print("Se agrego su producto")

def mostrar_inventario():
    if len(inventario) == 0:
        print("inventario vacio")
    else:
        for producto in inventario:
            producto.mostrar()

def vender_producto():
    nombre = input("que producto quieres vender?:")
    for producto in inventario:
        if producto.nombre.lower() == nombre.lower():
            cantidad = int(input("Cantidad a vender:"))
            producto.vender(cantidad)
            return
    print("producto no encontrado")


opcion = 0

while opcion != 4:
    print("\n--Tiendita--")
    print("1.-Agregar producto")
    print("2.-Mostrar inventario")
    print("3.-Vender producto")
    print("4.-Salir")

    opcion = int(input("que quieres hacer:"))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        vender_producto()
    elif opcion == 4:
        print("Programa finalizado")
        print("\nGracias por usar mi programa")
            

    
        
        
