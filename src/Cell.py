class Cell:
    def __init__(self, num):
        self.num = num
        self.row = None
        self.col = None
        self.region = None

        self.flag = False
        self.possibleNums = []

    def isValid(self):
        cellnum = self.num
        if self.row.countNum(cellnum) == 1 \
            and self.col.countNum(cellnum) == 1 \
                and self.region.countNum(cellnum) == 1:
            return True
        return False
