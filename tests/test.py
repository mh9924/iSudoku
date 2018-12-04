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
        randomPuzzles = self.openPuzzles("sudoku.csv")
        easyPuzzles = self.openPuzzles("sudoku-easy.csv")
        medPuzzles = self.openPuzzles("sudoku-med.csv")
        hardPuzzles = self.openPuzzles("sudoku-hard.csv")

        randomPuzzleObjs = []
        easyPuzzleObjs = []
        medPuzzleObjs = []
        hardPuzzleObjs = []

        n = 100
        randomPuzzles = randomPuzzles[:n]

        for puzzle in randomPuzzles:
            randomPuzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        for puzzle in easyPuzzles:
            easyPuzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        for puzzle in medPuzzles:
            medPuzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        for puzzle in hardPuzzles:
            hardPuzzleObjs.append(Puzzle.Puzzle(list(puzzle)))

        puzzleSets = [randomPuzzleObjs, easyPuzzleObjs, medPuzzleObjs, hardPuzzleObjs]
        i = 0
        names = ["RANDOM PUZZLES (n=" + str(n) + "):", "EASY PUZZLES:", "MEDIUM PUZZLES:", "HARD PUZZLES:"]

        for puzzleSet in puzzleSets:
            timeSum = 0
            timeMin = 0
            timeMax = 0

            print(names[i])
            print()

            for puzzleObj in puzzleSet:
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

            print("With " + str(len(puzzleSet)) + " puzzles: Took " + str(timeSum) + "s total")
            print("Average time per puzzle: " + str(timeSum / n) + "s")
            print("Minimum time a puzzle took: " + str(timeMin) + "s")
            print("Maximum time a puzzle took: " + str(timeMax) + "s")
            print()
            print()

            i += 1

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