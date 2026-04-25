def registrar_estudiante():
    """Registra un nuevo estudiante con nombre e ID."""  # Docstring: explica la función
    print("\n--- Registro de Estudiante ---")  # Muestra un encabezado en consola
    nombre = input("Ingrese el nombre del estudiante: ")  # Pide al usuario el nombre
    id_estudiante = input("Ingrese el ID del estudiante: ")  # Pide al usuario el ID
    # Aquí guardaremos los datos en una lista más adelante
    print(f"Estudiante {nombre} registrado con éxito.")  # Confirma el registro

def main():
    # Bucle principal del programa: se repite hasta que el usuario decida salir
    while True:
        print("\n1. Registrar Estudiante")  # Opción para registrar
        print("2. Salir")  # Opción para terminar el programa
        opcion = input("Seleccione una opción: ")  # Captura la elección del usuario
        
        if opcion == "1":
            registrar_estudiante()  # Llama a la función de registro
        elif opcion == "2":
            break  # Sale del bucle y termina el programa

# Punto de entrada del programa
if __name__ == "__main__":
    main()
