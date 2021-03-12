class AbilityScores:
    def __init__(self, strength):
        self.strength = strength
    
    def getStrengthMod(self):
        return (self.strength - 10) / 2