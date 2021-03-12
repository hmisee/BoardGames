from .src import character
from .src import size

class TestCharacter:
    fighter = character.Character("Herkules")
    fighter.setRace("Human")
    fighter.setClass("Fighter")
    fighter.setAbilityScores(16)

    def test_get_character_name(self):
        assert self.fighter.getName() == "Herkules"

    def test_get_character_race(self):
        assert self.fighter.getRace() == "Human"

    def test_get_character_class(self):
        assert self.fighter.getClass() == "Fighter"
    
    def test_get_size(self):
        assert self.fighter.getSize() == size.Size.MEDIUM

    def test_get_speed(self):
        assert self.fighter.getSpeed() == 30
    
    def test_get_strength_mod(self):
        assert self.fighter.getStrengthMod() == 3
