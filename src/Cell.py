class Cell:
    def __init__(self, num):
        self.num = num
        self.row = None
        self.col = None
        self.region = None

        self.flag = False
        self.possibleNums = []

    def isValid(self, cellnum):
        if not self.row.containsNum(cellnum) \
            and not self.col.containsNum(cellnum) \
                and not self.region.containsNum(cellnum):
            return True
        return False

    def isEmpty(self):
        return self.num == None