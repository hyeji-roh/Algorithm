import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
total = 0

for _ in range(N):
    heapq.heappush(heap, int(input()))

while True:
    if len(heap) == 1:
        break

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    tmp = a+b
    total += tmp

    heapq.heappush(heap, tmp)

print(total)