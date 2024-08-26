class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo_inventario):
        self.archivo_inventario = archivo_inventario
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = {}
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print(f"El archivo '{self.archivo_inventario}' no existe. Se creará uno nuevo al agregar productos.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for producto in self.productos.values():
                    archivo.write(str(producto) + '\n')
        except PermissionError:
            print(f"No se tiene permiso para escribir en '{self.archivo_inventario}'.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' agregado exitosamente.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad:
                producto.cantidad = cantidad
            if precio:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' actualizado exitosamente.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        else:
            print("El inventario está vacío.")

# Uso del sistema de gestión de inventarios
inventario = Inventario('inventario.txt')

# Agregar productos
inventario.agregar_producto(Producto('001', 'Manzanas', 50, 0.30))
inventario.agregar_producto(Producto('002', 'Naranjas', 30, 0.40))

# Mostrar inventario
inventario.mostrar_inventario()

# Actualizar un producto
inventario.actualizar_producto('001', cantidad=60)

# Mostrar inventario actualizado
inventario.mostrar_inventario()

# Eliminar un producto
inventario.eliminar_producto('002')

# Mostrar inventario final
inventario.mostrar_inventario()