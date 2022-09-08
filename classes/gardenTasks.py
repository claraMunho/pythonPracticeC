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



#Function for getting info about a garden
def getInfo(garden):
    return garden.__str__()

gardenia = Plant(1, 'Gardenia', 20, 'Medicinal', 'Decorative') #Add a plant
print(gardenia) #See gardenia details
# gardenia._uses = 'Beauty' #Doing this overrides the previous list of uses. We have to use the addUses method instead.
gardenia.addUses('Beauty') #Add a use to the plant
print(gardenia) #See the plant details again
print(f'Number of plants: {Plant.numberPlants}') #Find out how many plants we have right now
cactus = Plant(2,'Cactus', 0.1, 'Medicinal', 'Weapon') #Add a cactus to the plant list
garden1 = Garden(1, 200, gardenia, cactus) #Create a garden
print(garden1) #See garden details
Plant.addUses(gardenia,'Nutrients') #Add a use to gardenias
print(garden1) #New use is included in our garden
print(Garden.DEFAULT_FLUID) #Print class constant

#Testing processed products super class
aloeCream = ProcessedProducts(1, 'Aloe cream', 30, ('Beauty', 'Skin care'), 'Tin') #Add a processed product, which is a super class of Plant
print(aloeCream)
garden1 = Garden(None, 200, gardenia, cactus, aloeCream) #Add a processed product, super class of plant
print(garden1) #The garden has a processed product now
print(f'Remaining water: {watering(garden1,200)}')
print(f'Remaining water: {watering(garden1,20)}') #Testing not enough water exception

# print(getInfo(garden1))