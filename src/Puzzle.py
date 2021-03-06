from src import Cell
from src import Column
from src import Region
from src import Row

class Puzzle:
    def __init__(self, nums):
        if len(nums) != 81:
            print("Sudoku must be 9x9.")
            return

        self.cells = []
        self.rows = []
        self.cols = []
        self.regions = []

        self.buildGraph(nums)


    def buildGraph(self, nums):
        for i in range(0, 9):
            row = Row.Row()
            col = Column.Column()
            region = Region.Region()

            self.rows.append(row)
            self.cols.append(col)
            self.regions.append(region)

        colNo = 0
        rowNo = 0

        for n in nums:
            if isinstance(n, str):
                n = int(n)

            if n == 0:
                n = None
                
            if colNo == 9:
                colNo = 0
                rowNo += 1

            c = Cell.Cell(n)
            cellCol = self.cols[colNo]
            cellRow = self.rows[rowNo]
            cellRegion = self.regions[rowNo//3 * 3 + colNo//3]
            c.col = cellCol
            c.row = cellRow
            c.region = cellRegion

            self.cells.append(c)
            cellCol.cells.append(c)
            cellRow.cells.append(c)
            cellRegion.cells.append(c)

            colNo += 1

    def isValid(self):
        # Check if puzzle is valid and completed.
        for cell in self.cells:
            if not cell.isValid():
                return False

        return True

    def printSudoku(self):
        for r in self.rows:
            for c in r.cells:
                print("|", end="")

                if c.num is None:
                    print(" ", end="")
                else:
                    print(c.num, end="")

            print("|")

    def backtrackingSolve(self):
        c = None

        for cell in self.cells: # Iterate over each cell in the puzzle
            if cell.num is None:
                c = cell # Work with the first blank cell found.
                break

        if c is None: # If no empty cell is found, the puzzle is solved
            return True

        for candidate in range(1, 10):
            if c.isValidCandidate(candidate):
                c.num = candidate

                if self.backtrackingSolve(): # Recursively branch down possibilities for cell c
                    return True

                c.num = None

        return False

    def crooksAlgoSolve(self):
        c = None

        for cell in self.cells:  # cell.region will give the region object
            if cell.num != None:  # The cell object has something in it

                for cell in cell.row.cells:  # remove cell.num from the possible number list in the row
                    print(cell.num)
                    if cell.num in cell.possibleNums:
                        cell.possibleNums.remove(cell.num)
                for cell in cell.col.cells:  # remove cell.num from the possible number list in the column
                    if cell.num in cell.possibleNums:
                        cell.possibleNums.remove(cell.num)
            if cell.num is None:
                c = cell
                cell.num = c.possibleNums[0]
                if self.crooksAlgoSolve():
                    return True

                break

        if c is None:
            return True

        pass

        if c is None:
            return True


        pass

    def dancingLinksSolve(self):
        pass
