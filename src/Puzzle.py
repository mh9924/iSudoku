from src import Cell
from src import Column
from src import Region
from src import Row

class Puzzle:
    def __init__(self, nums):
        self.cells = []
        self.rows = []
        self.cols = []
        self.regions = []

        self.buildGraph(nums)


    def buildGraph(self, nums):
        for i in range(0, 9):
            row = Row()
            col = Column()
            region = Region()

            self.rows.append(row)
            self.cols.append(col)
            self.regions.append(region)

        i = 0
        for n in nums:
            c = Cell(n)
            self.cells.append(c)
            self.cols[i].cells.append(c)

            i += 1

    def backtrackingSolve(self):
        pass

    def crooksAlgoSolve(self):
        pass

    def dancingLinksSolve(self):
        pass