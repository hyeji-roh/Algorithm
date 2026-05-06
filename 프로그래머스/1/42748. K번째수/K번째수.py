def solution(array, commands):
    result = []
    for com in commands:
        arr = array[com[0]-1:com[1]]
        arr.sort()
        result.append(arr[com[2]-1])
    return result