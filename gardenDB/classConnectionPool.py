from logger_base import log
from psycopg2 import pool #Importamos pool de psycopg2
import sys


class ConexionPool:
    _DATABASE = 'pythonAprender' #Variables de clase privadas
    _USERNAME = 'postgres'
    _PASSWORD ='5858'
    _DB_PORT= '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1 #Número mínimo de objetos de tipo conexión
    _MAX_CON = 3
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(minconn = cls._MIN_CON,
                                                      maxconn = cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Conexión de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerraConexiones(cls):
        cls.obtenerPool().closeall()