class NotEnoughWater(Exception):
    def __init__(self, message): #Personalized message for this exeption
        self.message = message