import pyodbc



class Conexion:
    DATABASE='bdprueba'
    USERNAME='admin'
    PASSWORD='admin'
    DB_PORT='1433'
    SERVER='localhost'
    POOL_SIZE=5
    POOL_NAME='nombre_pool'
    pool=None

    @classmethod
    def get_conn(cls):
        if cls.pool is not None:
            return cls.pool
        else:
            try:
                connectionString = f'DRIVER={{SQL Server Native Client 11.0}};SERVER={cls.SERVER};DATABASE={cls.DATABASE};UID={cls.USERNAME};PWD={cls.PASSWORD}'
                cls.pool = pyodbc.connect(connectionString)
            ##    print(f'entro por aqui{cursor}')
                return cls.pool
            except:
                return f'error en conexion'

pool=Conexion.get_conn().cursor()
print(pool)