from sys import stdin
input = stdin.readline

def boj9734():
    from math import gcd

    while True:
        s = input().strip()
        if not s:
            break
        
        i = -1
        n = 0
        a = 1
        b = 1
        
        i += 1
        while s[i] != '.':
            n = n * 10 + (ord(s[i]) - 48)
            i += 1
        
        i += 1
        while s[i] != '(':
            n = n * 10 + (ord(s[i]) - 48)
            a *= 10
            i += 1
        
        i += 1
        while s[i] != ')':
            n = n * 10 + (ord(s[i]) - 48)
            b *= 10
            i += 1
        
        u = n - (n // b)
        d = a * (b - 1)
        
        g = gcd(u, d)
        u //= g
        d //= g
        
        print(f"{s} = {u} / {d}")

if __name__ == "__main__": boj9734()