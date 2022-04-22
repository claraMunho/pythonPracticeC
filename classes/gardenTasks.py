from classes.classPlant import Plant
from classes.classGarden import Garden
from classes.processedProducts import ProcessedProducts
from exceptions import NotEnoughWater

gardenia = Plant('Gardenia', 20, 'Medicinal', 'Decorative') #Add a plant
print(gardenia) #See gardenia details
# gard._uses = 'Beauty' #Doing this overrides the previous list of usses. We have to use the addUses method instead.
gardenia.addUses('Beauty') #Add a use to the plant
print(gardenia) #See the plant details again
print(f'Number of plants: {Plant.numberPlants}') #Find out how many plants we have right now
cactus = Plant('Cactus', 0.1, 'Medicinal', 'Weapon') #Add a cactus to the plant list
garden1 = Garden(200, gardenia, cactus) #Create a garden
print(garden1) #See garden details
Plant.addUses(gardenia,'Nutrients') #Add a use to gardenias
print(garden1) #New use is included in our garden
print(Garden.DEFAULT_FLUID) #Print class constant

aloeCream = ProcessedProducts('Aloe cream', 30, ('Beauty', 'Skin care'), 'Tin') #Add a processed product, which is a super class of Plant
print(aloeCream)
garden1 = Garden(200, gardenia, cactus, aloeCream) #Add a processed product, super class of plant
print(garden1) #The garden has a processed product now


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

print(f'Remaining water: {watering(garden1,200)}')

#Function for getting info about a garden
def getInfo(garden):
    return garden.__str__()

# print(getInfo(garden1))