# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    u_dict = dict()
    
    for r in record:
        r = r.split(" ")
        if r[0] in ['Enter', 'Change']:
            u_dict[r[1]] = r[2] # 마지막 입장한 id 저장
    
    for r in record:
        r = r.split(" ")
        if r[0] == 'Enter':
            answer.append("{0}님이 들어왔습니다.".format(u_dict[r[1]]))
        elif r[0] == 'Leave':
            answer.append("{0}님이 나갔습니다.".format(u_dict[r[1]]))
    return answer