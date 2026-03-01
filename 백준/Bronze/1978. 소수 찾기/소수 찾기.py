N = int(input())
arr = list(map(int, input().split()))
total = 0

for num in arr:
    flag = 0
    if num == 1:
        flag = 1
    for i in range(2, num):
        if num%i == 0:
            flag = 1
    if flag == 0:
        total += 1
print(total)