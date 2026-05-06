def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    print((sum(month[0:a])+b))
    return day[(sum(month[0:a])+b)%7]