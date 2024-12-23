from Persona import Persona
from conexion import Conexion


class PersonaDao:
    @classmethod
    def mostrar_personas(cls):
        conexion=None
        cursor=None
        try:
            conexion=Conexion.get_conn()
            cursor=conexion.cursor()
            cursor.execute(' select personaId,nombre,apellido from personas')
            registros=cursor.fetchall()
            personas=[]
            for registro in registros:
                persona=Persona(registro[0],registro[1],registro[2])
                personas.append(persona)
            return personas
        except Exception as e:
            print(f'Hay problemas de conexión: {e}')
        finally:
            if conexion is not None:
                if cursor is not None:
                    cursor.close()
            #    Conexion.liberar_conexion(conexion)

# if __name__ == '__main__':
#     personas=PersonaDao.mostrar_personas()
#     for persona in personas:
#         print(persona)