class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto for p in self.productos):
            print(f'Error: El ID {producto.get_id_producto()} ya existe.')
        else:
            self.productos.append(producto)
            print(f'Producto {producto.get_nombre()} añadido exitosamente.')

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        print(f'Producto con ID {id_producto} eliminado.')

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print(f'Producto con ID {id_producto} actualizado.')
                return
        print(f'Error: No se encontró el producto con ID {id_producto}.')

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f'No se encontraron productos con el nombre "{nombre}".')

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print('No hay productos en el inventario.')