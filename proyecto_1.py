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
        global ventas_dia
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            total = cantidad_vendida * self.precio
            ventas_dia += total
            print("------------Tiket------------")
            print("Producto:", self.nombre)
            print("Cantidad vendida", cantidad_vendida)
            print("total:", total)
            print("venta correcta, vuelva pronto")
            print("-----------------------------")
            if self.cantidad <= 5:
                print("Alerta, queda poco producto")
        else:
            print("no hay suficiente producto")
ventas_dia = 0
inventario = []
def mostrar_ventas():
     print("\n----- ventas del dia -----")
     print("Total vendido:$", ventas_dia)

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

def buscar_producto():

    nombre = input("Producto a buscar: ")

    for producto in inventario:

        if producto.nombre.lower() == nombre.lower():
            producto.mostrar()
            return

    print("Producto no encontrado")

opcion = 0

while opcion != 6:
    print("\n--Tiendita--")
    print("1.-Agregar producto")
    print("2.-Mostrar inventario")
    print("3.-Vender producto")
    print("4.-Buscar producto")
    print("5.-Mostrar ventas")
    print("6.-Salir")


    opcion = int(input("que quieres hacer:"))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        vender_producto()
    elif opcion == 4:
        buscar_producto()
    elif opcion == 5:
        mostrar_ventas()
    elif opcion == 6:
        print("programa finalizado")
        print("\ngracias por usar mi programa")
    else:
        print("opcion no valida")

    
        
        
