import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
print(sum(n*n for n in nums)%10)