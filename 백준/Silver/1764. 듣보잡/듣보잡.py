import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_n = set()
set_m = set()

result = []

for _ in range(N):
    set_n.add(input().strip())

for _ in range(M):
    set_m.add(input().strip())

print(len(set_n&set_m))

for name in set_n&set_m:
    result.append(name)

for name in sorted(result):
    print(name)