# Usando 'with' para abrir el archivo en modo lectura ('r').
try:
    with open('ejemplo_lectura.txt', 'r') as archivo:
        print(archivo.read())  # Imprime el contenido del archivo
except FileNotFoundError:
    print("El archivo 'ejemplo_lectura.txt' no se encontró.")

# Usando 'with' para abrir el archivo en modo escritura ('w') y crearlo si no existe.
# Escribe en él y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'w') as archivo:
    archivo.write('Este es un nuevo archivo.')  # Escribe en el archivo

# Usando 'with' para abrir el archivo en modo añadir ('a').
# Añade una nueva línea y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'a') as archivo:
    archivo.write('\nAñadiendo una segunda línea.')  # Añade nueva línea de texto

# Usando 'with' para abrir el archivo en modo lectura ('r').
try:
    with open('ejemplo_escritura.txt', 'r') as archivo:
        print(archivo.read())  # Imprime el contenido del archivo
except FileNotFoundError:
    print("El archivo 'ejemplo_escritura.txt' no se encontró.")