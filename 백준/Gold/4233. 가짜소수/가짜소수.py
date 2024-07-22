from sys import stdin
input = stdin.readline

def boj1612():
    def is_prime(n):
        if n<2: return False
        if n<4: return True
        if not n&1 or not n%3: return False
        i = 5
        while not i * i > n:
            if not n % i or not n % (i + 2): return False
            i += 6
        return True

    while True:
        p, a = map(int, input().split())
        if not p and not a: break
        print("yes") if pow(a, p, p) == a % p and not is_prime(p) else print("no")
        
if __name__ == '__main__': boj1612()