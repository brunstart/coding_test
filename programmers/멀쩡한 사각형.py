# 문제 url : https://programmers.co.kr/learn/courses/30/lessons/62048


def solution(n):
    answer = ''
    result = ''
    
    while n > 0:
        n, mod = divmod(n, 3)

        if mod == 0:
            n -= 1
            mod = 4
        result += str(mod)
                
    answer = result[::-1]
    
    return answer