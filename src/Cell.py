class Cell:
    def __init__(self, num):
        self.num = num
        self.row = None
        self.col = None
        self.region = None

        self.flag = False
        self.possibleNums = []


