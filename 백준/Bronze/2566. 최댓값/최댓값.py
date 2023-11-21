import sys

M=[]
mv = [0 for _ in range(3)]

for row in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    M.append(row)

for row in range(9):
    for col in range(9):
        if M[row][col]>=100 or M[row][col]<0: raise Exception(f'input error!')
        if mv[2] <= M[row][col]:
            mv[2] = M[row][col]
            mv[0] = row + 1
            mv[1] = col + 1

print(f'{mv[2]}\n{mv[0]} {mv[1]}')
