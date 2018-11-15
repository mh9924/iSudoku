class Puzzle:
    def __init__(self, nums):
        self.cells = []
        self.rows = []
        self.cols = []
        self.regions = []


    def isCellValid(self, cell):
        cellnum = cell.num
        if cell.row.countNum(cellnum) == 1 \
            and cell.col.countNum(cellnum) == 1 \
                and cell.region.countNum(cellnum) == 1:
            return True
        return False