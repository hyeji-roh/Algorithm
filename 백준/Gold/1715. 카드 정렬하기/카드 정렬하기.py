import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
result = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

while True:
    if len(heap) == 1:
        break

    tmp0 = heapq.heappop(heap)
    tmp1 = heapq.heappop(heap)
    result.append(tmp0)
    result.append(tmp1)

    heapq.heappush(heap, tmp0 + tmp1)

print(sum(result))