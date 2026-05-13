def solution(s):
    answer = [-1]*len(s)
    last = {}
    
    for idx, value in enumerate(s):
        if value in last:
            answer[idx] = idx-last[value]
        last[value] = idx
        
    return answer