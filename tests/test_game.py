from ..src.game import Game
from ..src.battle_map import BattleMap
from ..src.character import Character

class TestGame:
    def test_empty_map(self):
        battle_map = BattleMap(5,5)
        newGame = Game()
        newGame.addMap(battle_map)
        for cell in newGame.getMapCells():
            assert len(cell) == 0

    def test_put_character_on_map(self):
        battle_map = BattleMap(4,6)
        newGame = Game()
        newGame.addMap(battle_map)
        character = Character("Herkules")
        newGame.addCharcter(character, 1, 2)
        assert not len(newGame.getMapCells()[(2-1)*4 + (1-1)]) == 0
        for entity in newGame.getMapCells()[(2-1)*4 + (1-1)]:
            assert entity.getName() == "Herkules"
