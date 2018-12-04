class Cell:
    def __init__(self, num):
        self.num = num
        self.row = None
        self.col = None
        self.region = None

        self.flag = False
        self.possibleNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def isValidCandidate(self, cellnum):
        if not self.row.containsNum(cellnum) \
            and not self.col.containsNum(cellnum) \
                and not self.region.containsNum(cellnum):
            return True

        return False

    def isValid(self):
        if self.row.countNum(self.num) > 1 \
            or self.col.countNum(self.num) > 1 \
                or self.region.countNum(self.num) > 1:
            return False

        return True

    def isEmpty(self):
        return self.num == None