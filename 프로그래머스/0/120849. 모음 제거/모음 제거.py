def solution(my_string):
    answer = ''
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for word in my_string:
        if word not in aeiou:
            answer += word
    return answer