import sys
from collections import Counter

input = sys.stdin.readline

word = input().strip().upper()
cnt = Counter(word)

max_value = max(cnt.values())

result = [k for k, v in cnt.items() if v == max_value]

print("?" if len(result) > 1 else result[0])