from src import Puzzle


class SudokuTest:
    @staticmethod
    def backtracking():
        p = Puzzle.Puzzle(
            [8, None, None, 4, None, 6, None, None, 7,
            None, None, None, None, None, None, 4, None, None,
            None, 1, None, None, None, None, 6, 5, None,
            5, None, 9, None, 3, None, 7, 8, None,
            None, None, None, None, 7, None, None, None, None,
            None, 4, 8, None, 2, None, 1, None, 3,
            None, 5, 2, None, None, None, None, 9, None,
            None, None, 1, None, None, None, None, None, None,
            3, None, None, 9, None, 2, None, None, 5])

        p.printSudoku()

        p.backtrackingSolve()

        print()
        print("Solved via backtracking:")

        p.printSudoku()

test = SudokuTest()
test.backtracking()