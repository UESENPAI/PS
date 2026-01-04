from sys import stdin
input = stdin.readline

def boj22943():
    N = int(input().strip())
    MAXV = 999999

    is_prime = bytearray(b"\x01") * (MAXV + 1)
    is_prime[0] = is_prime[1] = 0
    p = 2
    while p * p <= MAXV:
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start:MAXV+1:step] = b"\x00" * (((MAXV - start) // step) + 1)
        p += 1


    prev = [0] * (N + 1)
    cur  = [0] * (N + 1)

    for i in range(1, N + 1):
        cur[0] = 0
        for j in range(1, N + 1):
            if i == 1 and j == 1:
                w = 0
            else:
                if j<10:
                    x = i * 10 + j
                elif j<100:
                    x = i * 100 + j
                else:
                    x = i * 1000 + j
                w = 1 if is_prime[x] else 0
            cur[j] = (prev[j] if prev[j] > cur[j-1] else cur[j-1]) + w
        prev, cur = cur, prev

    print(prev[N])

if __name__ == '__main__': boj22943()