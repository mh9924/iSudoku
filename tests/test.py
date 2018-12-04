from src import Puzzle
import time


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
        n = 1000

        for puzzle in puzzles[:n]:
            puzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        print("n = " + str(n))

        timeSum = 0
        timeMin = 0
        timeMax = 0

        for puzzleObj in puzzleObjs:
            print("------------------------------------")
            print()

            puzzleObj.printSudoku()

            start = time.time()
            puzzleObj.backtrackingSolve()
            end = time.time()
            timeTaken = end - start

            if timeMin == 0 or timeTaken < timeMin:
                timeMin = timeTaken

            if timeTaken > timeMax:
                timeMax = timeTaken

            print()
            print("Solved via backtracking in " + str(timeTaken) + "s")

            timeSum += timeTaken

            puzzleObj.printSudoku()
            print()

        print("With " + str(n) + " puzzles: Took " + str(timeSum) + "s total")
        print("Average time per puzzle: " + str(timeSum / n) + "s")
        print("Minimum time a puzzle took: " + str(timeMin) + "s")
        print("Maximum time a puzzle took: " + str(timeMax) + "s")

    def crooksAlgo(self):
        puzzles = self.openPuzzles("sudoku.csv")
        puzzleObj = Puzzle.Puzzle(list(puzzles[0]))

        puzzleObj.printSudoku()

        puzzleObj.crooksAlgoSolve()

    def dancingLinks(self):
        pass

test = SudokuTest()
test.backtracking()
# test.crooksAlgo()