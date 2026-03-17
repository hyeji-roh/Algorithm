n = int(input())
num = list(map(int, input().split()))
v = int(input())

result = 0

for i in num:
    if i == v:
        result+=1

print(result)