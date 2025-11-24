from sys import stdin
input = stdin.readline
 
def boj7869():
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    import math

    d = math.hypot(x1 - x2, y1 - y2)
    if d >= r1 + r2: area = 0.0
    elif d <= abs(r1 - r2): area = math.pi * min(r1, r2) ** 2
    else:
        phi = math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        theta = math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        area = r1**2 * phi + r2**2 * theta - 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    print(f"{area:.3f}")

if __name__ == '__main__': boj7869()