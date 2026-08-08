tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Mostrar progreso")
    print("4. Entrar de nuevo al programa")

def agregar_tarea():
    nombre = input("Tarea: ")
    tarea = {
        "nombre": nombre,
        "completada": False
    }
    tareas.append(tarea)

def listar_tareas():
    for tarea in tareas:
        print(
            tarea["nombre"],
            tarea["completada"]
        )