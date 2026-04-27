import json

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

def calcular_promedio():
    """Calcula el promedio y determina el estado del estudiante."""
    id_buscar = input("ID del estudiante para promedio: ")
    for estu in estudiantes:
        if estu["id"] == id_buscar:
            if not estu["notas"]:
                print("El estudiante no tiene notas registradas.")
                return
            promedio = sum(estu["notas"]) / len(estu["notas"])
            estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
            print(f"Promedio: {promedio:.2f} - Estado: {estado}")
            return
    print("Estudiante no encontrado.")

def generar_reporte():
    """Muestra una tabla con todos los estudiantes y sus resultados."""
    print("\n{:<10} {:<20} {:<15} {:<10}".format("ID", "Nombre", "Promedio", "Estado"))
    print("-" * 55)
    for estu in estudiantes:
        promedio = sum(estu["notas"]) / len(estu["notas"]) if estu["notas"] else 0
        estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
        print("{:<10} {:<20} {:<15.2f} {:<10}".format(estu["id"], estu["nombre"], promedio, estado))

def guardar_datos():
    """Guarda la lista de estudiantes en un archivo JSON."""
    with open("notas.json", "w") as f:
        json.dump(estudiantes, f, indent=4)
    print("Datos guardados en notas.json")

def cargar_datos():
    """Carga los datos desde el archivo JSON si existe."""
    global estudiantes
    try:
        with open("notas.json", "r") as f:
            estudiantes = json.load(f)
    except FileNotFoundError:
        estudiantes = [] 


def main():
    cargar_datos()  # Carga la información guardada al iniciar [cite: 36]
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
        print("1. Registrar Estudiante")
        print("2. Ingresar Notas")
        print("3. Calcular Promedio")
        print("4. Generar Reporte")
        print("5. Guardar y Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            ingresar_notas()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            guardar_datos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()