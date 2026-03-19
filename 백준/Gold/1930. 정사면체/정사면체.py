from sys import stdin
input = stdin.readline

def boj1930():
    K = int(input().strip())
    perms = [[0,1,2,3], [0,2,3,1], [0,3,1,2], [1,0,3,2], [1,3,2,0], [1,2,0,3], [2,0,1,3], [2,1,3,0], [2,3,0,1], [3,0,2,1], [3,2,1,0], [3,1,0,2]]
    results = []
    for _ in range(K):
        data = list(map(int, input().split()))
        a, b = data[:4], data[4:]
        same = any([b[p[0]], b[p[1]], b[p[2]], b[p[3]]] == a for p in perms)
        results.append('1' if same else '0')
    print('\n'.join(results))

if __name__ == '__main__': boj1930()