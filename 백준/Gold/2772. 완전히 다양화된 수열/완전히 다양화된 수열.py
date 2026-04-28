from sys import stdin
input = stdin.readline

def boj2772():
    out = []

    while True:
        n = int(input())
        if n == 0:
            break

        if n % 4 not in (0, 3):
            out.append("0")
            out.append("")
            continue

        sets = [None] + [list(range(i, n + 1)) for i in range(1, n + 1)]

        odd_indices = [
            i for i in range(1, n + 1)
            if (n - i + 1) % 2 == 1
        ]

        for i in range(0, len(odd_indices), 2):
            a = odd_indices[i]
            b = odd_indices[i + 1]

            x = a + 1

            sets[a].remove(x)
            sets[b].append(x)
            sets[b].sort()

        ans = sets[1:]
        ans.sort()

        out.append(str(n))
        for s in ans:
            out.append(" ".join(map(str, s)))
        out.append("")

    print("\n".join(out))

if __name__ == "__main__": boj2772()