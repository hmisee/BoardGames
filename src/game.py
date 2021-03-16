class Game:
    def addMap(self, battle_map):
        self.battle_map = battle_map
    def getMapCells(self):
        return self.battle_map.getCells()
    def addCharcter(self, character, x, y):
        self.battle_map.add(character, x, y)