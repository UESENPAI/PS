import sys
input = sys.stdin.readline

def boj10986():
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    res = [0 for _ in range(M)]
    res[0] = 1
    
    subsum = 0
    for a in range(len(A)):
        subsum += A[a]
        r = subsum % M
        res[r] += 1
    
    ans = 0
    for r in res:
        ans += r * (r - 1) // 2
    
    print(ans)

if __name__ == '__main__': boj10986()