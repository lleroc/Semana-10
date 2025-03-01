from alumnos import clase_alumnos
class clase_curso:
    def __init__(self, nombre:str = None, paralelo:str= None):
        self.nombre = nombre
        self.paralelo = paralelo
        self.lista_curso = []
    
    def agregar_curso_alumno(self, alumno:clase_alumnos):
        self.lista_curso.append(self.nombre, self.paralelo, alumno)
    
    def inforcacion(self):
        return self.lista_curso

