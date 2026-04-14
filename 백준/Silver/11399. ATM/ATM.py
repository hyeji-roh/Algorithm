import sys
input = sys.stdin.readline

N = int(input())

man = list(map(int, input().split()))
sort_man = sorted(man)
tmp = []

for i in range(0, len(sort_man)):
    tmp.append(sum(sort_man[0:i+1]))

print(sum(tmp))