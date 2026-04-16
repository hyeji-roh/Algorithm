def solution(array, height):
    cnt = 0
    for num in array:
        if num > height:
            cnt += 1
    return cnt