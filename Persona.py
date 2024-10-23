class Persona:
    def __init__(self,personaId=None,nombre=None,apellido=None,direccion=None,ciudad=None):
        self.personaId=personaId
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.ciudad=ciudad
    def __str__(self):
        return f''' id: {self.personaId}, nombre: {self.nombre}, apellido: {self.apellido} '''