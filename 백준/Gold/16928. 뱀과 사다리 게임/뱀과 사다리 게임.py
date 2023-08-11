import sys
from collections import deque
from math import inf
input = sys.stdin.readline
sys.setrecursionlimit(44444)

N, M = map(int, input().strip().split())

ladders = [(list(map(int, input().strip().split()))) for _ in range(N)]
snakes = [(list(map(int, input().strip().split()))) for _ in range(M)]

board = [inf for _ in range(101)]

dices = list(range(1,7))

def dfs(coord):
    global board
    for dice in dices:
        nextpos = (coord+dice) 
        if nextpos > 100: continue
        elif nextpos <= 100:
            if board[nextpos] > board[coord]+1:
                board[nextpos] = board[coord]+1
                for teleport in ladders+snakes:
                    if nextpos == teleport[0]:
                        nextpos = teleport[1]
                        board[nextpos] = board[coord]+1
                dfs(nextpos)
    return

board[1] = 0
dfs(1)
print(board[100])