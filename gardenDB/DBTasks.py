from DAOplants import plantDAO
from DAOgarden import GardenDAO
from logger_base import log
from classes.classPlant import Plant
from classes.classGarden import Garden

#Creating a plant, inserting it to the database (DB) and then selecting all the existing records in the DB.
plant1 = Plant(None, 'Aloe', 10, 'Medicine')
plantDAO.insert(plant1)
plantDAO.select()

#Creating a garden, inserting it to the DB and then selecting all the existing gardens in the DB.
garden1 = Garden(None, 20, plant1)
GardenDAO.insert(garden1)