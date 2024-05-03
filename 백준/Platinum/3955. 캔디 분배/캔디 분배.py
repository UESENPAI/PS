import sys
input = sys.stdin.readline

def boj2608():
    t = int(input().strip())
    KC = [tuple(map(int, input().strip().split())) for _ in range(t)]
    UBOUND = 10**9

    def get_gcd(k, c):
        if not c: return k, 1, 0
        gcd, x, y = get_gcd(c, k % c)
        return gcd, y, x - (k // c) * y


    results = []
    for k, c in KC:
        if c == 1:
            results.append("IMPOSSIBLE" if k + 1 > UBOUND else k + 1)
            continue

        if k == 1:
            results.append(1)
            continue
         
        if not k % c:
            results.append("IMPOSSIBLE") if (k + 1) % c else results.append((k + 1) // c)
            continue
        else:
            gcd, x, y = get_gcd(k, c)
            if gcd!=1:
                results.append("IMPOSSIBLE")
                continue
            else:
                X = (x%c * (c - 1)) % c
                bags = (k * X + 1) // c
                results.append("IMPOSSIBLE") if bags > UBOUND else results.append(bags)    
  
    for result in results: print(result)

if __name__ == '__main__': boj2608()
