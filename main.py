estudiantes = []

def registrar_estudiante():
    """Registra un nuevo estudiante y lo añade a la lista."""
    nombre = input("Nombre del estudiante: ")
    id_estu = input("ID del estudiante: ")
    estudiantes.append({"id": id_estu, "nombre": nombre, "notas": []})
    print(f"Estudiante {nombre} registrado.")

def ingresar_notas():
    """Busca un estudiante por ID e ingresa sus notas (0-5)."""
    id_buscar = input("Ingrese el ID del estudiante para calificar: ")
    for estu in estudiantes:
        if estu["id"] == id_buscar:
            try:
                nota = float(input(f"Ingrese la nota para {estu['nombre']} (0-5): "))
                if 0 <= nota <= 5:
                    estu["notas"].append(nota)
                    print("Nota agregada con éxito.")
                else:
                    print("Error: La nota debe estar entre 0 y 5.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
            return
    print("Estudiante no encontrado.")