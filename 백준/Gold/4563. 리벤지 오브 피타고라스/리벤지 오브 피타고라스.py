from sys import stdin
input = stdin.readline


def boj4563():
    data = map(int, stdin.read().split())
    out = []
    for A in data:
        if not A: break

        A2 = A * A
        cnt = 0

        for x in range(1, A + 1):
            if A2 % x: continue
            y = A2 // x
            diff = y - x
            if diff & 1: continue
            B = diff >> 1
            if B > A: cnt += 1

        out.append(str(cnt))

    print("\n".join(out))

if __name__ == "__main__": boj4563()