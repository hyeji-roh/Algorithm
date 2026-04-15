import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_s = set()
cnt = 0

for _ in range(N):
    n_s.add(input())

for _ in range(M):
    word = input()

    if word in n_s:
        cnt += 1

print(cnt)