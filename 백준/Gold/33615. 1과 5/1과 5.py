from sys import stdin
input = stdin.readline

def boj33615():
    T = int(input())
    for _ in range(T):
        s = input().strip()

        sum_mod3 = 0
        first_one = -1
        first_five = -1

        for i, c in enumerate(s):
            if c == '1':
                sum_mod3 += 1
                if first_one == -1:
                    first_one = i + 1
            else:
                sum_mod3 += 2
                if first_five == -1:
                    first_five = i + 1

        sum_mod3 %= 3

        if sum_mod3 == 0:
            print(0, 3)
            continue

        if first_five == -1:
            if len(s) % 2 == 0:
                print(0, 11)
            else:
                print(1, 11)
            continue

        if first_one == -1:
            print(0, 5)
            continue

        if sum_mod3 == 1:
            print(first_one, 3)
        else:
            print(first_five, 3)

if __name__ == "__main__":
    boj33615()