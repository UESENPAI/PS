
def boj11571():
    T = int(input())
    ab = [list(map(int, input().split())) for _ in range(T)]

    def printf(a, b):
        if not a%b:
            print(f"{a // b}.(0)")
            return
        ans = f"{a // b}."
        a%=b
        buffer = {}
        rem = ""

        idx = 0
        while a:
            if a in buffer:
                ptr = buffer[a]
                nr, r = rem[:ptr], rem[ptr:]
                print(f"{ans}{nr}(0)") if r == "0" else print(f"{ans}{nr}({r})")
                return

            buffer[a] = idx
            a *= 10
            rem += str(a // b)
            a %= b
            idx += 1

        ans += rem
        print(f"{ans}(0)")
    
    for a, b in ab: printf(a, b)

if __name__ == "__main__": boj11571()