def registrar_estudiante():
    """Registra un nuevo estudiante con nombre e ID."""
    print("\n--- Registro de Estudiante ---")
    nombre = input("Ingrese el nombre del estudiante: ")
    id_estudiante = input("Ingrese el ID del estudiante: ")
    print(f"Estudiante {nombre} registrado con éxito.")

def main():
    while True:
        print("\n1. Registrar Estudiante")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            break

if __name__ == "__main__":
    main()
