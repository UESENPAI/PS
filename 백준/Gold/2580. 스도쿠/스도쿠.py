import sys

sudoku = []
zeros = []
for rowidx in range(9):
    row = (list(map(int,sys.stdin.readline().strip().split())))
    for colidx in range(9):
        if row[colidx]==0:
            zeros.append((rowidx, colidx))
    sudoku.append(row)

def checkRow(x, a):
    global sudoku
    for i in range(9):
        if a == sudoku[x][i]:
            return False
    return True

def checkCol(y, a):
    global sudoku
    for i in range(9):
        if a == sudoku[i][y]:
            return False
    return True

def checkRect(x, y, a):
    global sudoku
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sudoku[nx+i][ny+j]:
                return False
    return True

def displaysudoku(sudoku):
    for row in sudoku:
        print(' '.join(map(str, row)))

def dfs(idx):
    global sudoku, zeros
    
    if idx == len(zeros):
        displaysudoku(sudoku)
        exit(0)

    for i in range(1, 10):
        x = zeros[idx][0]
        y = zeros[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sudoku[x][y] = i
            dfs(idx+1)
            sudoku[x][y] = 0

dfs(0)
