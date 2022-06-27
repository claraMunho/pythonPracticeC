from classConnectionPool import ConexionPool
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self): #Este método se manda a llamar cuando se inicia el bloque with
        log.debug('Inicio del método with __enter__')
        self._conexion = ConexionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb): #Cambiado los valores por defecto: tipo, valor y traceback (=detalle de excepción)
        log.debug('Se ejecuta método __exit__')
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción: {exc_val} {exc_type} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
            self._cursor.close()
            ConexionPool.liberarConexion(self._conexion)