from classes.classPlant import Plant

class ProcessedProducts(Plant): #Superclass
    def __init__(self, plantName, waterIntake, uses, packaging):
        super().__init__(plantName, waterIntake, uses)
        self.packaging = packaging
    def __str__(self):
        return f'{super().__str__()} is packed in a {self.packaging}'

