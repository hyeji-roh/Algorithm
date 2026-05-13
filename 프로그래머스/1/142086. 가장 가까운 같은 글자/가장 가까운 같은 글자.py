def solution(s):
    tmp = ''
    answer = [-1]*len(s)
    
    for idx in range(len(s)):
        if s[idx] in tmp:
            print("s[idx]", s[idx])
            answer[idx] = tmp[::-1].index(s[idx])+1
        tmp += s[idx]
            
    return answer