from sys import stdin
input = stdin.readline

def boj1876():
    import math
    
    n = int(input())

    for _ in range(n):
        T, X = input().split()
        T = float(T)
        X = int(X)

        theta = math.radians(X)
        target = T * 100.0
        margin = 16.0 / math.sin(theta)
        left = target - margin
        right = target + margin
        step = 85.0 / math.tan(theta)
        dist = 0.0
        hit = False

        while dist <= right:
            if left <= dist <= right:
                hit = True
                break
            dist += step

        print("yes" if hit else "no")

if __name__ == "__main__": boj1876()