import sys

input = sys.stdin.readline

N = int(input())
num = input().strip()

print(sum(map(int, num)))