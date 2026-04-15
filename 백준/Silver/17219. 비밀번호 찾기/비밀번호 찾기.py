import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = {}

for _ in range(N):
    name, pw = input().strip().split()
    d[name] =  pw

for _ in range(M):
    name = input().strip()
    print(d[name])