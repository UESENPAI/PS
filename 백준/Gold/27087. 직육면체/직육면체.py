from sys import stdin, stdout
input = stdin.readline
 
def bo27087():
    T = int(input())
    for _ in range(T):
        A, B, C, p = map(int, input().split())
        print(int((not A % p) + (not B % p) + (not C % p) > 1))

if __name__ == '__main__': bo27087()