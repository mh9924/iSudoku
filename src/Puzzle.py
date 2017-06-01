class Puzzle:
    def __init__(self, nums):
        self.nums = nums
        self.cells = {}
        self.possiblenums = {}
        self.numrows = 9  # Not testing for different sizes yet
        self.numcols = 9
        self.numboxes = 9
        self.size = self.numrows*self.numcols
        self.buildGraph()

    def buildGraph(self):
        self.rows = [[] for i in range(self.numrows)]
        self.cols = [[] for i in range(self.numcols)]
        self.boxes = [[] for i in range(self.numboxes)]
        row = 97
        col = 1
        for k,num in enumerate(self.nums):
            self.cols[k % self.numcols].append(num)
            self.rows[k // self.numrows].append(num)
            self.boxes[((k % self.numcols) // 3) + ((k // self.numrows) // 3) * 3].append(num)
            self.cells[str(chr(row))+str(col)] = num
            if col == self.numcols:
                row += 1
                col = 0
            col += 1

    def getIndexByCell(self, cell):
        return ((ord(cell[0])-97)*self.numboxes) + (int(cell[1:])-1)

    def updateNumByCell(self, cell, num):
        self.nums[self.getIndexByCell(cell)] = num
        self.cells[cell] = num
        self.buildGraph()

    def appendNumByCell(self, cell, num):
        self.cells[cell].append(num)
        self.buildGraph()

    def getNumByCell(self, cell):
        return self.cells[cell]

    def getRowByCell(self, cell):
        return self.rows[ord(cell[0])-97]

    def getColByCell(self, cell):
        return self.cols[int(cell[1:])-1]

    def getBoxByCell(self, cell):
        return self.boxes[((self.getIndexByCell(cell) % self.numcols) // 3) + ((self.getIndexByCell(cell) // self.numrows) // 3) * 3]

    def isCellValid(self, cell):
        cellnum = self.getNumByCell(cell)
        if self.getRowByCell(cell).count(cellnum) == 1 \
            and self.getColByCell(cell).count(cellnum) == 1 \
                and self.getBoxByCell(cell).count(cellnum) == 1:
            return True
        return False

    def findPossibleValues(self):
        for key in self.cells:
            if self.getNumByCell(key) is None:
                self.updateNumByCell(key, [])
            if isinstance(self.getNumByCell(key), list):
                cellpossibles = []
                for x in range(1, 10):
                    if x not in self.getRowByCell(key) \
                        and x not in self.getColByCell(key)\
                            and x not in self.getBoxByCell(key):
                        self.appendNumByCell(key, x)
                        cellpossibles.append(x)
                self.possiblenums[key] = cellpossibles

    def solve(self):
        for k,v in self.possiblenums.items():
            if len(self.possiblenums[k]) == 1:
                self.updateNumByCell(k, self.possiblenums[k][0])
                # Implement algorithm