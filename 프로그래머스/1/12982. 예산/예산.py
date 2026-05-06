def solution(d, budget):
    d.sort() 

    start = 0
    end = len(d)

    for _ in range(len(d)):
        if sum(d[start:end]) <= budget:
            return end - start
        else:
            end -= 1

    return 0 