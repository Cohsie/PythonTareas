# Clase base para las frutas
class Fruta:
    def __init__(self, nombre, precio, descuento=0):
        """Constructor que inicializa el nombre, precio y descuento de la fruta."""
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def precio_final(self):
        """Calcula el precio final de la fruta con descuento."""
        return round(self.precio * (1 - self.descuento / 100), 2)

    def __str__(self):
        """Representación en cadena para mostrar los detalles de la fruta."""
        return f"{self.nombre}: Precio: ${self.precio}, Descuento: {self.descuento}%, Precio Final: ${self.precio_final()}"

# Diccionario para almacenar las frutas
frutas = {}

# Función para mostrar el menú
def mostrar_menu():
    """Muestra las opciones del menú al usuario."""
    print("\n--- Menú ---")
    print("1. Añadir fruta")
    print("2. Ver frutas")
    print("3. Modificar fruta")
    print("4. Eliminar fruta")
    print("5. Ordenar frutas por precio")
    print("6. Ver detalles de una fruta")
    print("7. Salir")

# Función para añadir una fruta al diccionario
def añadir_fruta():
    """Permite añadir una fruta al diccionario con nombre, precio y descuento."""
    nombre = input("Introduce el nombre de la fruta: ").strip()
    
    # Validación de precio y descuento
    while True:
        try:
            precio = float(input("Introduce el precio de la fruta: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")
    
    while True:
        try:
            descuento = float(input("Introduce el descuento de la fruta (en %): "))
            if descuento < 0:
                raise ValueError("El descuento no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")
    
    # Crear una instancia de la fruta y añadirla al diccionario
    fruta = Fruta(nombre, precio, descuento)
    frutas[nombre] = fruta
    print(f"Fruta {nombre} añadida exitosamente.")

# Función para ver todas las frutas
def ver_frutas():
    """Muestra todas las frutas registradas en el diccionario."""
    if not frutas:
        print("No hay frutas registradas.")
    else:
        print("\n--- Lista de frutas ---")
        for nombre, fruta in frutas.items():
            print(f"{nombre}: {fruta}")

# Función para modificar una fruta existente
def modificar_fruta():
    """Permite modificar el precio o descuento de una fruta."""
    nombre = input("Introduce el nombre de la fruta que deseas modificar: ").strip()
    if nombre in frutas:
        print(f"Fruta encontrada: {frutas[nombre]}")
        
        # Modificar precio
        while True:
            try:
                nuevo_precio = float(input("Introduce el nuevo precio de la fruta: "))
                if nuevo_precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        
        # Modificar descuento
        while True:
            try:
                nuevo_descuento = float(input("Introduce el nuevo descuento de la fruta (en %): "))
                if nuevo_descuento < 0:
                    raise ValueError("El descuento no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        
        # Actualizar la fruta
        frutas[nombre].precio = nuevo_precio
        frutas[nombre].descuento = nuevo_descuento
        print(f"Fruta {nombre} modificada exitosamente.")
    else:
        print("La fruta no existe en el registro.")

# Función para eliminar una fruta
def eliminar_fruta():
    """Permite eliminar una fruta del diccionario."""
    nombre = input("Introduce el nombre de la fruta que deseas eliminar: ").strip()
    if nombre in frutas:
        del frutas[nombre]
        print(f"Fruta {nombre} eliminada exitosamente.")
    else:
        print("La fruta no existe en el registro.")

# Función para ordenar frutas por precio
def ordenar_frutas():
    """Ordena las frutas en el diccionario por su precio y muestra el resultado."""
    if frutas:
        frutas_ordenadas = sorted(frutas.values(), key=lambda x: x.precio)
        print("\n--- Frutas ordenadas por precio ---")
        for fruta in frutas_ordenadas:
            print(fruta)
    else:
        print("No hay frutas registradas para ordenar.")

# Función para ver los detalles de una fruta específica
def ver_detalles_fruta():
    """Muestra los detalles completos de una fruta específica."""
    nombre = input("Introduce el nombre de la fruta para ver detalles: ").strip()
    if nombre in frutas:
        print(frutas[nombre])
    else:
        print("La fruta no existe en el registro.")

# Función principal para ejecutar el programa
def main():
    """Función principal que ejecuta el bucle del menú."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1/2/3/4/5/6/7): ")

        if opcion == "1":
            añadir_fruta()
        elif opcion == "2":
            ver_frutas()
        elif opcion == "3":
            modificar_fruta()
        elif opcion == "4":
            eliminar_fruta()
        elif opcion == "5":
            ordenar_frutas()
        elif opcion == "6":
            ver_detalles_fruta()
        elif opcion == "7":
            confirmacion = input("¿Estás seguro que deseas salir? (s/n): ").strip().lower()
            if confirmacion == "s":
                print("¡Hasta luego!")
                break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
