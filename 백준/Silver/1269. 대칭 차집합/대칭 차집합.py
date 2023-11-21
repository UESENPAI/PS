import sys

A, B = map(int,sys.stdin.readline().split())

setA = set(map(int,sys.stdin.readline().split()))

setB = set(map(int,sys.stdin.readline().split()))

print(f'{len(set.difference(set.union(setA,setB), set.intersection(setA,setB)))}')
