from src import Puzzle


class SudokuTest:

    def openPuzzles(self, dataFileName):
        puzzles = []
        lines = open(dataFileName).readlines()

        for line in lines:
            columns = line.split(",")
            unsolved = columns[0]
            puzzles.append(unsolved)

        return puzzles


    def backtracking(self):
        puzzles = self.openPuzzles("sudoku.csv")
        puzzleObjs = []

        for puzzle in puzzles[:10]:
            puzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        print(len(puzzleObjs))
        print(puzzleObjs[0].cells[2].num)

        for puzzleObj in puzzleObjs:
            print("------------------------------------")
            print()

            puzzleObj.printSudoku()
            puzzleObj.backtrackingSolve()

            print()
            print("Solved via backtracking:")

            puzzleObj.printSudoku()
            print()

    def crooksAlgo(self):
        puzzles = self.openPuzzles("sudoku.csv")
        puzzleObj = Puzzle.Puzzle(list(puzzles[0]))

        puzzleObj.crooksAlgoSolve()

    def dancingLinks(self):
        pass

test = SudokuTest()
#test.backtracking()
test.crooksAlgo()