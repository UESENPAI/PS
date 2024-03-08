import sys
input = sys.stdin.readline

def boj1041():
    N = int(input().strip())
    dice = list(map(int, input().strip().split()))
    if N==1: print(sum(dice)-max(dice))
    else:
        cases = sorted([min(dice[d], dice[5-d]) for d in range(3)])
        f3 = 4 * sum(cases[:3])
        f2 = (4*(N-2) + 4*(N-1)) * sum(cases[:2])
        f1 = ((N-2)*(N-2) + 4*(N-2)*(N-1)) * sum(cases[:1])
        print(f1+f2+f3)

if __name__ == '__main__': boj1041()