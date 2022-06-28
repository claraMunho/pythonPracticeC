from classConnectionPool import ConexionPool
from classCursor import CursorDelPool
from classes.classPlant import Plant
from logger_base import log

class plantDAO:
    _SELECT = 'SELECT * FROM plant'
    _INSERT = 'INSERT INTO plant(plant_name, water_intake, uses) VALUES(%s, %s, %s)'

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            recs = cursor.fetchall()
            plants = []
            for rec in recs:
                plant = Plant(rec[1],rec[0], rec[2], rec[3])
                plants.append(plant)
                log.debug(f'Plant name: {plant.plantName}')
            return plants
    @classmethod
    def insert(cls, plant):
        with CursorDelPool() as cursor:
            values = plant.plantName, plant.waterIntake, plant.uses
            cursor.execute(cls._INSERT, values)
            log.debug(f'Plant inserted: {plant}')
            return cursor.rowcount