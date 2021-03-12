from . import size
from .ability_scores import AbilityScores

class Character:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRace(self, race):
        self.race = race

    def getRace(self):
        return self.race

    def setClass(self, ch_class):
        self.ch_class = ch_class

    def getClass(self):
        return self.ch_class
    
    def getSize(self):
        return size.Size.MEDIUM

    def getSpeed(self):
        return 30
    
    def setAbilityScores(self, strength):
        self.abilityScores = AbilityScores(strength)
    
    def getStrengthMod(self):
        return self.abilityScores.getStrengthMod()