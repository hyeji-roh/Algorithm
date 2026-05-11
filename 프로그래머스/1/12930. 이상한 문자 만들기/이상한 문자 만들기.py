def solution(s):
    answer = ''
    idx = 0

    for ch in s:
        if ch == ' ':
            answer += ' '
            idx = 0

        elif idx % 2 == 0:
            answer += ch.upper()
            idx += 1

        else:
            answer += ch.lower()
            idx += 1

    return answer