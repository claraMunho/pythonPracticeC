from classConnectionPool import ConexionPool
from classCursor import CursorDelPool
from classes.classGarden import Garden
from logger_base import log

class GardenDAO:
    _SELECT = 'SELECT * FROM garden ORDER BY garden_id'
    _INSERT = 'INSERT INTO garden(surface, plants) VALUES (%s, %s)'
    _DELETE = 'DELETE FROM garden WHERE garden_id = %s'
    _UPDATE = 'UPDATE garden SET surface = %s, plants = %s WHERE garden_id = %s'

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            recs = cursor.fetchall()
            gardens = []
            for rec in recs:
                # plantsList = ['Con','Ver']
                    # list(rec[1])
                garden = Garden(rec[2], rec[0], rec[1])
                gardens.append(garden)
            return gardens

    @classmethod
    def insert(cls, garden):
        with CursorDelPool() as cursor:
            values = (garden.surface, 'Aloe')
            cursor.execute(cls._INSERT, values)
            log.debug(f'Garden inserted: {garden.idGarden}. Surface: {garden.surface}')
            return cursor.rowcount

# if __name__ == '__main__':
#     #Select
#     gardens = GardenDAO.select()
#     for garden in gardens:
#         log.debug(garden)

def converStrToList(*strngs):
    strToList = [str for str in strngs]
    log.debug(strToList)
    return strToList

def convertListToStr(lst):
    strngJoined = '|'.join(str(e) for e in lst)
    return strngJoined
#Tests for conversion functions
strngConverted = converStrToList('Ho', 'La')
print(convertListToStr(strngConverted))