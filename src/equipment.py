
class EquipementType:
    MARTIAL=1
    MELEE=2
    WEAPON=3

class Equipment:
    def __init__(self, name):
        self.name = name
        self.types = [EquipementType.MARTIAL, EquipementType.MELEE, EquipementType.WEAPON]