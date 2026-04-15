import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))

counter = Counter(n_arr)

M = int(input())
m_arr = list(map(int, input().split()))

result = []

for num in m_arr:
    result.append(str(counter[num]))

print(' '.join(result))