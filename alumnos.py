from datetime import datetime
class clase_alumnos:  #listas []
    def __init__(self,id:int = None, nombre= None, apellido= None, telefono= None, fecha:datetime =""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
