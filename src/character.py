from . import size
from .ability_scores import AbilityScores
from .equipment import EquipementType

class Character:
    def __init__(self, name):
        self.name = name
        self.proficiencies = [EquipementType.MARTIAL]
        self.proficiencyBonus = 2
        self.equipments = []
        self.left_hand = 0

    def getName(self):
        return self.name

    def getSize(self):
        return size.Size.MEDIUM

    def getSpeed(self):
        return 30
    
    def setAbilityScores(self, strength):
        self.abilityScores = AbilityScores(strength)

    def addEquipment(self, equipment):
        if equipment not in self.equipments:
            self.equipments.append(equipment)
        
    def equip(self, equipment):
        if EquipementType.WEAPON in equipment.types:
            if self.left_hand == 0:
                self.left_hand = equipment

    def getAttackMod(self):
        for prof in self.left_hand.types:
            if prof in self.proficiencies:
                return self.proficiencyBonus + self.abilityScores.getStrengthMod()
        return self.abilityScores.getStrengthMod()

    def getDamageMod(self):
        return 0