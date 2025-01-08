# Clase Producto
class Producto:
    def __init__(self, nombre, precio, categoria):
        """Constructor que inicializa los atributos del producto."""
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        """Representación en cadena de la información del producto."""
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Categoría: {self.categoria}"


# Diccionario para almacenar los productos
productos = {}

# Función para añadir un producto al diccionario
def añadir_producto():
    """Permite añadir un producto al diccionario."""
    nombre = input("Introduce el nombre del producto: ").strip()
    
    # Validación de entrada para el precio
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")

    categoria = input("Introduce la categoría del producto: ").strip()
    
    # Crear una instancia de Producto y añadirla al diccionario
    producto = Producto(nombre, precio, categoria)
    productos[nombre] = producto
    print(f"Producto '{nombre}' añadido exitosamente.")

# Función para mostrar los productos
def ver_productos():
    """Muestra todos los productos en el diccionario."""
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de productos ---")
        for nombre, producto in productos.items():
            print(f"{nombre}: {producto}")

# Menú interactivo
def menu():
    """Muestra un menú para gestionar los productos."""
    while True:
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Ver productos")
        print("3. Salir")

        opcion = input("Elige una opción (1/2/3): ").strip()

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
