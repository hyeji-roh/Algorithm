def solution(A,B):
    A_sorted = sorted(A)
    B_sorted = sorted(B, reverse=True)
    result = 0
    
    for i in range(len(A)):
        result += (A_sorted[i]*B_sorted[i])
    
    return result