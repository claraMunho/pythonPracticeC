from wateringManagement import watering
from classes.classGarden import *

#Function for getting info about a garden
def getInfo(garden):
    return garden.__str__()

#Retrieve garden info and print it to garden files
def retrieveGardenInfo(garden):
    print('Retrieving info from garden'.center(50,'-'))
    gardenStr = getInfo(garden)
    remainingWater = watering(garden,200)
    try:
        gardenFile = open('gardenFiles.txt', 'w', encoding = 'utf8')
        gardenFile.write(f'{gardenStr} \n')
        gardenFile.write(f'Remaining water: {remainingWater}')
    except Exception as e:
        print(e)
    finally:
        gardenFile.close()
        print('File closed'.center(50,'-'))