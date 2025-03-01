from alumnos import clase_alumnos
from cursos import clase_curso

alumno = clase_alumnos()
curso = clase_curso()
while True:
        print("-" * 20)
        print("-------------Bienvenido al Sistema de Distribicion de Cursos--------------")
        print("Lista de Opciones")
        print("1. Crear un Alumno")
        print("2. Crear un Curso") 
        print("3. Asignar el alumno al curso")
        print("4. Lista de Cursos y Alumnos")
        print("4. Salir")

        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            id = 0
            nombre = input("Ingrese el Nombre: ")
            apellido = input("Ingrese el Apellido: ")
            telefono = input("Ingrese el Telefono: ")
            alumno = clase_alumnos(id,nombre,apellido,telefono)
        if opcion == 2:
            nombre_curso = input("Ingrese el Nombre del Curso: ")
            paralelo = input("Ingrese el Paralelo: ")
            curso = clase_curso(nombre,paralelo)
        if opcion == 3:
            curso.agregar_curso_alumno(alumno)
        if opcion == 4:
             print(curso.inforcacion())
        if opcion == 5:
             print("Gracias por su colaboracion")
             break

                
