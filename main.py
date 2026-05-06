estudiantes = []

def registrar_estudiante():
    """Registra un estudiante y lo almacena en memoria."""
    nombre = input("Nombre del estudiante: ")
    id_estu = input("ID del estudiante: ")
    estudiantes.append({"id": id_estu, "nombre": nombre, "notas": []})
    print(f"Estudiante {nombre} registrado.")

def ingresar_notas():
    """Permite ingresar notas válidas (0 a 5) a un estudiante."""
    id_buscar = input("Ingrese el ID del estudiante: ")
    for estu in estudiantes:
        if estu["id"] == id_buscar:
            try:
                nota = float(input("Ingrese la nota (0-5): "))
                if 0 <= nota <= 5:
                    estu["notas"].append(nota)
                    print("Nota agregada correctamente.")
                else:
                    print("Error: nota fuera de rango.")
            except ValueError:
                print("Error: debe ingresar un número.")
            return
    print("Estudiante no encontrado.")
