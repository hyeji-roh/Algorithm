N, K = map(int, input().split())
n_total = 1
k_total = 1

for num in range(N, N-K, -1):
    n_total *= num

for kum in range(K, 1, -1):
    k_total *= kum

print(n_total//k_total)