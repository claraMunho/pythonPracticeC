class Plant:
    
    numberPlants = 0
    @classmethod
    def countPlants(cls):
        cls.numberPlants += 1
        return cls.numberPlants

    def __init__(self, idPlant, plantName, waterIntake, *uses):
        self._idPlant = idPlant
        self._numberPlants = Plant.countPlants()
        self._plantName = plantName
        self._waterIntake = waterIntake
        self._uses = list(uses)
    def __str__(self):
        return f'Id. {self._idPlant} Name: {self._plantName}. Water intake: {self._waterIntake} liters per month. Uses: {self._uses}'

    @property
    def idPlant(self):
        return self.idPlant

    @idPlant.setter
    def idPlant(self, idPlant):
        self.idPlant = idPlant

    @property
    def plantName(self):
        return self._plantName
    @plantName.setter
    def plantName(self, plantName):
        self._plantName = plantName
    @property
    def waterIntake(self):
        return self._waterIntake
    @waterIntake.setter
    def waterIntake(self, waterIntake):
        self._waterIntake = waterIntake
    @property
    def uses(self):
        return self._uses
    @uses.setter
    def uses(self, uses):
        self._uses = uses
        
    # def seePlantDetails(self): #No need for this because we have set the string method
    #     print(f'Name: {self._plantName}. Water intake: {self._waterIntake} liters per month. Uses: {self._uses}')

    def addUses(self, use):
        self._uses.append(use)