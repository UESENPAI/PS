import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def boj1963():
    T = int(input().strip())
    TC = [list(map(int,input().strip().split())) for _ in range(T)]

    def getEratoSieve():
        primes = [True for _ in range(10000)]
        p = 2
        while (p * p < 10000):
            if (primes[p] == True):
                for i in range(p * p, 10000, p): primes[i] = False
            p += 1
        return [p for p in range(1000, 10000) if primes[p]]

    primes = getEratoSieve()

    def getGraph(primes):

        def isConnected(num1, num2):
            num1, num2 = str(num1), str(num2)
            cnt = 0
            for i in range(len(num1)):
                if num1[i] != num2[i]: cnt += 1
            return cnt == 1
        
        graph = defaultdict(list)
        for prime in primes:
            for nxtprime in primes:
                if isConnected(prime, nxtprime):
                    graph[prime].append(nxtprime)
        return graph

    graph = getGraph(primes)

    def bfs(start, end):
        nonlocal graph
        dist = {prime: None for prime in graph}
        dist[start] = 0
        q = deque([start])
        while q:
            ptr = q.popleft()
            for nxt in graph[ptr]:
                if dist[nxt] is None:
                    q.append(nxt)
                    dist[nxt] = dist[ptr] + 1
                    if nxt == end: return dist[nxt]
        return "Impossible"

    for tc in TC: print(bfs(tc[0], tc[1])) if tc[0]!= tc[1] else print(0)

if __name__ == '__main__': boj1963()