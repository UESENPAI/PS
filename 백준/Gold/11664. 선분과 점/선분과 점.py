from sys import stdin
from math import sqrt
input = stdin.readline

def boj11664():
    Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(float, input().split())

    ABx, ABy, ABz = Bx - Ax, By - Ay, Bz - Az
    ACx, ACy, ACz = Cx - Ax, Cy - Ay, Cz - Az

    dot_AC_AB = ACx * ABx + ACy * ABy + ACz * ABz
    dot_AB_AB = ABx * ABx + ABy * ABy + ABz * ABz

    t = dot_AC_AB / dot_AB_AB

    if t < 0: t = 0
    elif t > 1: t = 1

    Px, Py, Pz = Ax + t * ABx, Ay + t * ABy, Az + t * ABz

    distance = sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2 + (Pz - Cz) ** 2)

    print(f"{distance:.6f}")

if __name__ == '__main__': boj11664()