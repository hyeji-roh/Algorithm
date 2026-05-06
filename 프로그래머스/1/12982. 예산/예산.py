def solution(d, budget):
    d = sorted(d)
    result = 0
    tmp = 0
    
    for value in d:
        if tmp < budget:
            tmp += value
            if tmp <= budget:
                result += 1
            else:
                break
    return result
    