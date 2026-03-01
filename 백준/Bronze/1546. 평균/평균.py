M = int(input())
score = list(map(int, input().split()))

max_score = max(score)
total = 0

for n in score:
    total += (n/max_score)

print(total/len(score)*100)