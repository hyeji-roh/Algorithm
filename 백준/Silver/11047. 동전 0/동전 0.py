n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

for value in coin[::-1]:
    if k == 0:
        break
    elif k >= value :
        pin = k//value
        k -= value*pin
        cnt += pin
    else:
        continue
        
print(cnt)