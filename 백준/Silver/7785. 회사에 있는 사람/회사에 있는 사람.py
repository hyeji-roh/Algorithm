import sys

input = sys.stdin.readline

N = int(input())
d = {}

for _ in range(N):
    name, status = map(str, input().split())
    
    if status == "leave":
        del d[name]
    else:
        d[name] = status

for key in sorted(d, reverse=True):
    print(key)