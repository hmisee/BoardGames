from .src import character

def test_get_character_name():
    fighter = character.Character("Herkules", "Human")
    assert fighter.getName() == "Herkules"

def test_get_character_race():
    fighter = character.Character("Herkules", "Human")
    assert fighter.getRace() == "Human"