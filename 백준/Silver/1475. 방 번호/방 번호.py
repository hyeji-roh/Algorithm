n = list(input())
arr = [0]*10

for i in n:
    arr[int(i)] += 1

six_nine = arr[6]+arr[9]

if six_nine % 2 == 0:
    arr[6] = arr[9] = six_nine//2
else:
    arr[6] = arr[9] = (six_nine//2)+1

print(max(arr))