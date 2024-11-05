import sys
input = sys.stdin.readline

def boj11729():
    def hanoi(n, start, end, mid, moves):
        if n == 1:
            moves.append((start, end))
        else:
            hanoi(n - 1, start, mid, end, moves)
            moves.append((start, end))
            hanoi(n - 1, mid, end, start, moves)

    N = int(input().strip())
    moves = []
    hanoi(N, 1, 3, 2, moves)
    print(len(moves))
    for move in moves: print(move[0], move[1])

if __name__ == "__main__": boj11729()
