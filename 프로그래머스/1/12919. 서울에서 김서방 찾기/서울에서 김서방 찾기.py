def solution(seoul):
    result = 0
    for word in seoul:
        if word == "Kim":
            result = seoul.index(word)
    return "김서방은 %d에 있다"%result