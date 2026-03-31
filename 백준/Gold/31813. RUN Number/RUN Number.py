from sys import stdin
input = stdin.readline

def boj31813():
    runs = []
    for length in range(1, 18):
        for d in range(1, 10):
            runs.append(int(str(d) * length))

    runs.sort(reverse=True)

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        
        res = []
        for r in runs:
            if not K: break
            if r <= K:
                res.append(r)
                K -= r
        
        print(len(res))
        print(*res)

if __name__ == "__main__": boj31813()