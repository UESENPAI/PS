import sys
input = sys.stdin.readline

def boj10253():
    T = int(input().strip())    
    ab = [list(map(int, input().strip().split())) for _ in range(T)]

    def getx(a, b, visited):
        x = b // a
        x += 1 if b % a else 0
        while x in visited: x += 1
        return x

    for a, b in ab:
        visited = set()
        if a != 1:
            while True:
                x = getx(a, b, visited)
                a *= x
                a -= b
                b *= x
                visited.add(x)
                if not a: break
        else: x = b
        print(x)

if __name__ == '__main__': boj10253()