'''Sistema de calificaciones.'''

# creamos una lista vacía para almacenar los estudiantes y sus calificaciones
students = []
# creamos un diccionario con la nota mínima para aprobar
rules = {"min_pass_grade" : 3.0}


# ===== Función para agregar un nuevo estudiante =====
def add_student():

    # solicitamos el ID del estudiante
    id_student = input("Ingrese el ID del estudiante -->").strip()

    # verificamos que el id no exista ya en la lista
    for student in students:
        if student["id"] == id_student :
            print("Ya existe un estudiante con ese ID.")
            return # salimos de la función si el id ya existe
    
    # solicitamos el nombre y apellido del estudiante
    name_student = input("Ingrese el nombre del estudiante -->").strip()
    lastname_student = input("Ingrese el apellido del estudiante -->").strip()

    
        
    # si el id no existe, creamos un diccionario para agregar el estudiante a la lista
    new_student = {
        "id": id_student,
        "name": name_student,
        "lastname": lastname_student,
        "subjects": {} # diccionario vacío para las asignaturas y sus notas
    }

    students.append(new_student)
    print(f"Estudiante '({id_student}) {name_student} {lastname_student}' agregado con éxito.")


# ===== Función para registrar notas de un estudiante =====
def register_grade():
    # solicitamos el ID del estudiante
    id_student = input("Ingrese el ID del estudiante -->").strip()

    # buscamos el estudiante en la lista, si no existe, mostramos un mensaje de error
    student = next((s for s in students if s["id"] == id_student), None)
    if not student:
        print(f"No se encontró un estudiante con el ID '{id_student}'.")
        return
    
    # solicitamos el nombre de la asignatura
    name_subject = input("Ingrese el nombre de la asignatura -->").strip().lower()

    # si la asignatura no existe, la creamos dentro del diccionario de asignaturas del estudiante
    if name_subject not in student["subjects"]:
        student["subjects"][name_subject] = []

    # solicitamos la nota
    grade = input("Ingrese la nota obtenida -->").strip()
    # validamos que la nota sea un número válido 
    if not grade.replace(".", "", 1).isnumeric():
        print("Por favor ingrese una nota válida.")
        return
    
    # convertimos la nota a float
    grade = float(grade)

    # validamos que la nota esté en el rango permitido (0 a 5)
    if grade < 0 or grade > 5:
        print("La nota debe estar entre 0 y 5.")
        return
        
    # agregamos la nota a la asignatura del estudiante
    student["subjects"][name_subject].append(grade)
    print(f"Nota {grade} registrada para la asignatura '{name_subject}' del estudiante '{student['name']} {student['lastname']}'.")


# ===== Función para editar notas de un estudiante =====
def update_grade():
    # solicitamos el ID del estudiante
    id_student = input("Ingrese el ID del estudiante -->").strip()

    # buscamos el estudiante en la lista, si no existe, mostramos un mensaje de error
    student = next((s for s in students if s["id"] == id_student), None)
    if not student:
        print(f"No se encontró un estudiante con el ID '{id_student}'.")
        return
    
    # solicitamos el nombre de la asignatura a editar
    name_subject = input("Ingrese el nombre de la asignatura -->").strip().lower()

    # verificamos que la asignatura exista
    if name_subject not in student["subjects"]:
        print(f"La asignatura '{name_subject}' no existe para el estudiante '{student['name']} {student['lastname']}'.")
        return
    
    # mostramos las notas actuales para esa asignatura
    print(f"Notas actuales para '{name_subject}': {student['subjects'][name_subject]}")

    # solicitamos la nota a editar
    old_grade = input("Ingrese la nota que desea editar -->").strip()

    # validamos que la nota sea un número válido
    if not old_grade.replace(".", "", 1).isnumeric():
        print("Por favor ingrese una nota válida.")
        return
    
    # convertimos la nota a float
    old_grade = float(old_grade)

    # verificamos que la nota exista en la lista de notas de la asignatura
    if old_grade not in student["subjects"][name_subject]:
        print(f"La nota {old_grade} no existe en la asignatura '{name_subject}'.")
        return
    
    # solicitamos la nueva nota
    new_grade = input("Ingrese la nueva nota -->").strip()

    # validamos que la nueva nota sea un número válido
    if not new_grade.replace(".", "", 1).isnumeric():
        print("Por favor ingrese una nota válida.")
        return
    
    # convertimos la nueva nota a float
    new_grade = float(new_grade)

    # validamos que la nueva nota esté en el rango permitido (0 a 5)
    if new_grade < 0 or new_grade > 5:
        print("La nota debe estar entre 0 y 5.")
        return
    
    # localizamos el índice de la nota antigua y la reemplazamos por la nueva
    index = student["subjects"][name_subject].index(old_grade)
    student["subjects"][name_subject][index] = new_grade

    print(f"Nota {old_grade} actualizada a {new_grade} para la asignatura '{name_subject}' del estudiante '{student['name']} {student['lastname']}'.")


# ===== Función para mostrar reportes de aprobados y reprobados =====
def show_reports():
    if not students:
        # verificamos si hay estudiantes registrados
        print("No hay estudiantes registrados.")
        return
    
    # tomamos el valor del umbral de aprobación desde el diccionario de reglas
    limit = rules.get("min_pass_grade", 3.0)

    print("\n===== REPORTES DE ESTUDIANTES =====")

    # recorremos todos los estudiantes registrados
    for student in students:
        name_student = student.get("name", "Desconocido")
        lastname_student = student.get("lastname", "")
        subjects = student.get("subjects", {})

        # interpolamos nombre y apellido para mostrar
        full_name = f"{name_student} {lastname_student}".strip()
        print(f"\nEstudiante: {full_name} (ID: {student['id']})")

        # verificamos si el estudiante tiene asignaturas registradas
        if not subjects:
            print("  No hay asignaturas registradas.")
            continue
        
        # lista para almacenar los promedios por asignatura
        subjects_average = [] 

        
        for name_subject, grades in subjects.items():
            # verificamos si hay notas registradas para la asignatura
            if not grades:
                print(f"  Asignatura: {name_subject.capitalize()} - No hay notas registradas.")
                continue

            # calculamos el promedio de la asignatura
            average_sub = sum(grades) / len(grades)
            subjects_average.append(average_sub)

            # mostramos el promedio de la asignatura y el estado (aprobado/reprobado)
            print(f"  Asignatura: {name_subject.capitalize()} - Promedio: {average_sub:.2f} - {'Aprobado' if average_sub >= limit else 'Reprobado'}")
        
        # si no hay notas en ninguna asignatura, evitamos dividir por cero
        if not subjects_average:
            print("  No hay notas registradas en ninguna asignatura.")
            continue

        # calculamos el promedio general del estudiante
        overall_average = sum(subjects_average) / len(subjects_average)

        # determinamos si aprueba o no según el promedio general
        status = "Aprobado" if overall_average >= limit else "Reprobado"

        # mostramos el promedio general y el estado final del estudiante
        print(f"\n  Promedio General: {overall_average:.2f} | Umbral: {limit} | Estado: {status}")


# ===== Menú principal =====

while True:
    # mostramos el menú de opciones
    print("===== SISTEMA DE CALIFICACIONES =====")
    print("1) Agregar Estudiante\n2) Registrar notas\n3) Editar notas\n4) Reportes (aprobados/reprobados)\n5) Salir")

    # solicitamos la opción al usuario
    option=input("\nIngresa una opción ->").strip()

    # validamos que la entrada sea numérica y esté dentro del rango de opciones
    if not option.isnumeric() or option not in ["1", "2", "3", "4", "5"]:
        print("Por favor ingrese una opción válida.")
        continue # volvemos a pedir el dato

    # convertimos la entrada a entero
    option = int(option)

    # usamos match para las opciones del menú. Definimos las funciones fuera del match para mayor claridad.
    # ejecutamos la función correspondiente según la opción seleccionada
    match option:
        
        case 1:
            add_student()
        case 2:
            register_grade()
        case 3:
            update_grade()
        case 4:
            show_reports()
        case 5:
            print("¡Hasta la próxima!")
            break # salimos del bucle y terminamos el programa
