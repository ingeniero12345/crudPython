class conexion:
    DATABASE='nombreDatabase'
    USERNAME='root'
    PASSWORD='admin'
    DB_PORT='4300'
    HOST='localhost'
    POOL_SIZE=5
    POOL_NAME='nombre_pool'
    pool=None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool=pooling
            except: