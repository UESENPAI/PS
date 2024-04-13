import sys
input = sys.stdin.readline

def boj1017():
    N = int(input().strip())
    numbers = tuple(map(int,input().strip().split()))

    def getPrimes(N):
        isprime = [False for _ in range(N+1)]
        p = 2
        while p * p < N+1:
            if not isprime[p]:
                for i in range(p * p, N+1, p): isprime[i] = True
            p += 1     
        return [i for i in range(2, N+1) if not isprime[i]]

    def findPrimePairs():
        nonlocal N, numbers
        primes = set(getPrimes(max(numbers)<<1))
        isPrimePair = lambda a, b: a + b in primes
        pairs = []
        for i in range(N):
            for j in range(i + 1, N):
                if isPrimePair(numbers[i], numbers[j]):
                    pairs.append((numbers[i], numbers[j]))
        
        return sorted(pairs)

    primePairs = findPrimePairs()

    def bipartite():
        nonlocal numbers, primePairs
        
        def dfs(x, visited, graph, match):
            try:
                if visited[x]: return False
            except KeyError:
                return False
            visited[x] = True
            for i in graph[x]:
                if match[i] == -1 or dfs(match[i], visited, graph, match):
                    match[i] = x
                    return True
            return False
        
        answers = []
        Primes = getPrimes(max(numbers)<<1)
        graph = {num: [] for num in numbers}
        for i in range(N):
            for j in range(i+1, N):
                if numbers[i] + numbers[j] in Primes:
                    graph[numbers[i]].append(numbers[j])
                    graph[numbers[j]].append(numbers[i])

        x0 = numbers[0]
        for fx0 in graph[x0]:
            subNumbers = [num for num in numbers if num!= x0 and num!= fx0]
            match = {num: -1 for num in numbers}
            match[x0] = fx0
            success = True
            for x in subNumbers:
                visited = {num: False for num in subNumbers}
                if not dfs(x, visited, graph, match):
                    success = False
                    break
            if success: answers.append(fx0)

        return sorted(answers) if answers else [-1]

    print(' '.join(map(str, bipartite())))


if __name__ == '__main__': boj1017()