class BattleMap:
    def __init__(self, x, y):
        self.rows = []
        for i in range(y):
            row = []
            for j in range(x):
                row.append([])
            self.rows.append(row)
    
    def getCells(self):
        cells = []
        for row in self.rows:
            for cell in row:
                cells.append(cell)
        return cells
    
    def add(self, entity, x, y):
        self.rows[y-1][x-1].append(entity)