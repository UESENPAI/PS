import sys
input = sys.stdin.readline

def boj1484():
    N = int(input().strip())

    def getWeight(N):
        results = []
        for xMy in range(1, N+1):
            if not N % xMy:
                xPy = N // xMy
                if not (xPy+xMy)%2 and not (xPy-xMy)%2:
                    x, y = (xPy+xMy) >> 1, (xPy-xMy) >> 1
                    if y > 0: results.append(x)

        return sorted(results) if results else [-1]

    ans = getWeight(N)
    print("\n".join(map(str, ans)))

if __name__ == '__main__': boj1484()