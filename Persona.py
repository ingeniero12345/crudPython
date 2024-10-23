class Persona:
    def __init__(self,personaId=None,nombre=None,apellido=None,direccion=None,ciudad=None):
        self.__personaId=personaId
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.ciudad=ciudad
    def get_personaId(self):
        return self.__personaId
    def __str__(self):
        return f''' id: {self.get_personaId()}, nombre: {self.nombre}, apellido: {self.apellido} '''