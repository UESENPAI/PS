import sys
from math import sqrt
from itertools import combinations
input = sys.stdin.readline

def boj1405():
    T = int(input().strip())

    def getVecLength(v): return sqrt(v[0]**2 + v[1]**2)
    
    def getVecSum(vectors):
        v = [sum(x) for x in zip(*vectors)]
        return getVecLength(v)

    for _ in range(T):
        N = int(input().strip())
        points = [tuple(map(int, input().strip().split())) for _ in range(N)]

        ans = sys.maxsize
        for combination in combinations(range(N), (N>>1)):
            vectors = []
            remnants = set(range(N)) - set(combination)
            
            for c in combination:
                point1, point2 = points[c], points[remnants.pop()]
                vector = (point2[0] - point1[0], point2[1] - point1[1])
                vectors.append(vector)
                
            ans = min(ans, getVecSum(vectors))
            
        print(ans)

if __name__ == '__main__': boj1405()