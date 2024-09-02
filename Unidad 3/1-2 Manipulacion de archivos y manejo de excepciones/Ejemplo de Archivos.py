class Inventario:
    def __init__(self, archivo_inventario='inventario.txt'):
        self.archivo_inventario = archivo_inventario
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    nombre, cantidad = linea.strip().split(',')
                    self.productos[nombre] = int(cantidad)
        except FileNotFoundError:
            print(f"Archivo {self.archivo_inventario} no encontrado, creando un nuevo archivo.")
            open(self.archivo_inventario, 'w').close()
        except PermissionError:
            print(f"No se tiene permiso para leer el archivo {self.archivo_inventario}.")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for nombre, cantidad in self.productos.items():
                    archivo.write(f"{nombre},{cantidad}\n")
        except PermissionError:
            print(f"No se tiene permiso para escribir en el archivo {self.archivo_inventario}.")

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto {nombre} añadido/actualizado exitosamente.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto {nombre} eliminado exitosamente.")
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")