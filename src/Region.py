class Region:
    def __init__(self):
        self.cells = []

    def containsNum(self, num):
        for c in self.cells:
            if c.num == num:
                return True
        return False

    def countNum(self, num):
        count = 0
        for c in self.cells:
            if c.num == num:
                count += 1
        return count
