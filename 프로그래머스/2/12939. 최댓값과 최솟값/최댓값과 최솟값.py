def solution(s):
    tmp = list(map(int, s.split(' ')))
    tmp.sort()
    return str(tmp[0])+' '+str(tmp[-1])