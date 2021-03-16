from ..src.game import Game
from ..src.battle_map import BattleMap
from ..src.character import Character

NUMBER_OF_ROWS=6
NUMBER_OF_COLUMNS=4
class TestGame:
    newGame = Game()
    battle_map = BattleMap(NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)
    newGame.addMap(battle_map)
    def test_empty_map(self):
        for cell in self.newGame.getMapCells():
            assert len(cell) == 0

    def test_put_character_on_map(self):
        character = Character("Herkules")
        self.newGame.addCharcter(character, 1, 2)
        character_cell = self.newGame.getMapCells()[(2)*NUMBER_OF_COLUMNS + (1)]
        assert not len(character_cell) == 0
        for entity in character_cell:
            assert entity.getName() == "Herkules"
