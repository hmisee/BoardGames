from .src import character

def test_get_character_name():
    fighter = character.Character("Herkules")
    assert fighter.getName() == "Herkules"