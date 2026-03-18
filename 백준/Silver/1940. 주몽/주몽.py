n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
left = 0
right = len(arr)-1

while left < right:
    total = arr[left] + arr[right]
    if total == m:
        cnt += 1
        left += 1
        right -= 1
    elif total < m:
        left += 1
    else:
        right -=1

print(cnt)