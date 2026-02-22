N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for answer in sorted(arr, key=lambda x: (x[1], x[0])):
    print(answer[0], answer[1])