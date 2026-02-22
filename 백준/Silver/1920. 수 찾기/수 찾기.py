N = int(input())
N_arr = set(map(int, input().split()))

M = int(input())
M_arr = list(map(int, input().split()))

for num in M_arr:
    print(1) if num in N_arr else print(0)