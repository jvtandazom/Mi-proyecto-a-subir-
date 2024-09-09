# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Usando tupla para titulo y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return f"{self.nombre} no tiene libros prestados."
        return "\n".join([str(libro) for libro in self.libros_prestados])


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurar IDs únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' agregado a la biblioteca.")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.titulo_autor[0]}' eliminado de la biblioteca.")
        else:
            print("El libro con ese ISBN no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está en uso.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            self.usuarios[id_usuario].prestar_libro(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {self.usuarios[id_usuario].nombre}.")
        else:
            print("El libro o el usuario no existen.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
                    return
            print("Este usuario no tiene prestado ese libro.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo in libro.titulo_autor[0]) or \
               (autor and autor in libro.titulo_autor[1]) or \
               (categoria and categoria == libro.categoria):
                resultados.append(str(libro))
        return resultados if resultados else "No se encontraron libros con esos criterios."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
    libro2 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

    # Agregar libros
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuario
    usuario1 = Usuario("Jonathan Tandazo", "U123")
    biblioteca.registrar_usuario(usuario1)

    # Prestar libro
    biblioteca.prestar_libro("978-0-452-28423-4", "U123")

    # Listar libros prestados
    print(usuario1.listar_libros_prestados())

    # Devolver libro
    biblioteca.devolver_libro("978-0-452-28423-4", "U123")

    # Buscar libros por autor
    resultados = biblioteca.buscar_libro(autor="George Orwell")
    print("\n".join(resultados))
