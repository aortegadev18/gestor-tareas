tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Mostrar progreso")
    print("4. Salir")

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


def mostrar_progreso():
    total = len(tareas)
    if total == 0:
        print("Sin tareas")
        return

    completadas = 0
    for tarea in tareas:
        if tarea["completada"]:
            completadas += 1

    porcentaje = (
        completadas * 100 / total
    )
    print(porcentaje, "%")