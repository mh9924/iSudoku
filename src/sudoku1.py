from itertools import product
import time

start_time = time.time()

def solve_sudoku(size, grid):



    #Creates size, ie (3, 3)
    R, C = size
    #Creates grid length ie 3*3=9
    N = R * C
    #Creates initial array using 4 cartesian products going from 0-9
    X = ([("rc", rc) for rc in product(range(N), range(N))] +
         [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
         [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
         [("bn", bn) for bn in product(range(N), range(1, N + 1))])
    #Creates an empty dictionary
    Y = dict()

    #Creates variables r, c, and n. r and c range 0-9, where n ranges 1-10 (ie N+1)
    for r, c, n in product(range(N), range(N), range(1, N + 1)):
        #Creates b which is the box # (ie (6/3)*3) + (6/3) = 6+2 = 8)
        b = (r // R) * R + (c // C)
        #Adds to dictionary Y the general form of the array X,
        #but including n and b (hence the cell titles)
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
    #Re-creates X and Y using exact_cover
    X, Y = exact_cover(X, Y)

    #Enumerate adds a number list to array items
    #Creates i and row variables that goes through the grid
    for i, row in enumerate(grid):
        #Creates j and n variables that go through the row
        for j, n in enumerate(row):
            if n:
                #Calls select function
                select(X, Y, (i, j, n))

    #Creates solution while calling solve function for X, Y, and an empty array            
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid

def exact_cover(X, Y):
    #Creates a subset j within X
    X = {j: set() for j in X}
    
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y

def solve(X, Y, solution):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

'''grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
for solution in solve_sudoku((3, 3), grid):
    print(*solution, sep='\n')'''

grid = [
        [0, 8, 0, 5, 1, 0, 0, 3, 0],
        [0, 0, 3, 0, 0, 7, 9, 0, 8],
        [0, 9, 0, 0, 0, 3, 0, 0, 0],
        [6, 0, 0, 2, 0, 4, 0, 0, 1],
        [0, 5, 0, 0, 0, 0, 0, 2, 0],
        [1, 0, 0, 9, 0, 8, 0, 0, 5],
        [0, 0, 0, 7, 0, 0, 0, 8, 0],
        [7, 0, 1, 8, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 9, 1, 0, 5, 0]]


for solution in solve_sudoku((3, 3), grid):
    print(*solution, sep='\n')


solved = []
for solution in solve_sudoku((3, 3), grid):
    solved.append(solution)
print(solved)
print ("My program took", time.time() - start_time, "seconds to run")
