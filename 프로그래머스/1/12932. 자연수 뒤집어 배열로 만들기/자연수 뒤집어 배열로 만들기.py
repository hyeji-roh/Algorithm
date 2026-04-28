def solution(n):
    n = str(n)[::-1]
    answer = []
    for num in n:
        answer.append(int(num))
    return answer