from sys import stdin
input = stdin.readline

perms = [[0,1,2,3], [0,2,3,1], [0,3,1,2],[1,0,3,2], [1,3,2,0], [1,2,0,3],[2,0,1,3], [2,1,3,0], [2,3,0,1],[3,0,2,1], [3,2,1,0], [3,1,0,2]]

def canonical(t):
    return min(
        tuple(t[p[i]] for i in range(4))
        for p in perms
    )

def boj1930():
    K = int(input().strip())
    res = []

    for _ in range(K):
        data = list(map(int, input().split()))
        a, b = data[:4], data[4:]
        res.append('1' if canonical(a) == canonical(b) else '0')

    print('\n'.join(res))

if __name__ == '__main__': boj1930()