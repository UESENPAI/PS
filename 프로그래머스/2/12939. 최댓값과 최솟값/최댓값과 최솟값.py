def solution(s):
    s = [int(x) for x in s.split()]
    answer = f'{min(s)} {max(s)}'
    return answer