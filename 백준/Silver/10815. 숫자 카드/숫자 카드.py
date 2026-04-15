import sys
input = sys.stdin.readline

N = int(input())
n_arr = set(map(int, input().split()))

M = int(input())
m_arr = set(map(int, input().split()))

result = []

for num in m_arr:
    if num in n_arr:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))