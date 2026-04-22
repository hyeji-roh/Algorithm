def solution(n):
    n = str(n)
    arr = sorted(list(n), reverse=True)
    return int(''.join(arr))