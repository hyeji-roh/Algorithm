a = int(input())
b = int(input())
c = int(input())

result = a*b*c

tmp = list(str(result))
arr = [0]*10

for t in tmp:
    arr[int(t)] += 1

for num in arr:
    print(num)
