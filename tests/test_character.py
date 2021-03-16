from ..src import character
from ..src import size
from ..src.equipment import Equipment

class TestCharacter:
    fighter = character.Character("Herkules")
    fighter.setAbilityScores(16)
    fighter.addEquipment(Equipment("Pike"))
    fighter.equip(Equipment("Pike"))

    def test_get_character_name(self):
        assert self.fighter.getName() == "Herkules"
    
    def test_get_size(self):
        assert self.fighter.getSize() == size.Size.MEDIUM

    def test_get_speed(self):
        assert self.fighter.getSpeed() == 30

    def test_attack_mod(self):
        assert self.fighter.getAttackMod() == 5
    
    def test_damage_mod(self):
        assert self.fighter.getDamageMod() == 0