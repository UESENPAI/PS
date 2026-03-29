from sys import stdin
input = stdin.readline

def boj25908():
    S, T = map(int, input().split())

    def cnt(x: int) -> int:
        ret = 0
        l = 1

        while l <= x:
            v = x // l
            r = x // v

            even = (r>>1) - ((l - 1)>>1)
            length = r - l + 1
            odd = length - even

            ret += (even - odd) * v

            l = r + 1

        return ret

    print(cnt(T) - cnt(S - 1))

if __name__ == '__main__': boj25908()