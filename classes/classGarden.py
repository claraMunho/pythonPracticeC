class Garden:
    DEFAULT_FLUID = 'H20' #Class constant
    def __init__(self, idGarden, surface, *plants):
        self._idGarden = idGarden
        self._surface = surface
        self._plants = list(plants)

    @property
    def idGarden(self):
        return self.idGarden
    @idGarden.setter
    def idGarden(self, idGarden):
        self._idGarden = idGarden
    @property
    def surface(self):
        return self._surface
    @surface.setter
    def surface(self, surface):
        self._surface = surface
    @property
    def plants(self):
        return self._plants
    @plants.setter
    def plants(self, *plants):
        self._plants = list(plants)

    def __str__(self):
        plantsList = ''
        for pl in self._plants:
            plantsList += pl.__str__() + '\n'
        return f'This garden has a surface of {self._surface} meters. \nPlants: {plantsList} \nNeeded water: {self.neededWater()} \nId: {self._idGarden}'

    def neededWater(self):
        waterNeed = 0.00
        for pl in self._plants:
            waterNeed += pl._waterIntake
        return waterNeed