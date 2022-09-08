from classes.classPlant import Plant
from classes.classGarden import Garden
from classes.classProcessedProducts import ProcessedProducts
from exceptions import NotEnoughWater

#Watering a garden
def watering(garden, availableWater):
    need = garden.neededWater()
    try:
        if need >= availableWater:
            raise NotEnoughWater('Not enough water!')
    except Exception as e:
        print(f'{e}') #, type(e))
    else:
        availableWater -= need
    return availableWater