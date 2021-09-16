# 문제 url : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    enter = '님이 들어왔습니다.'
    leave = '님이 나갔습니다.'
    name = {}
    
    for i in record:
        if len(i.split()) >= 3:
            name[i.split()[1]] = i.split()[2]
            
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append(name[i.split()[1]]+enter)
        elif i.split()[0] == 'Leave':
            answer.append(name[i.split()[1]]+leave)
    
    
    return answer


test_case = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234","Enter uid1234 Prodo",
                "Change uid4567 Ryan"]

answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", 
            "Prodo님이 들어왔습니다."]

print(bool(solution(test_case) == answer))