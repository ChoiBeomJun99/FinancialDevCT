# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 방법1
def solution(progresses, speeds):
    takes_days = []
    answer = []
    cnt = 0
    
    for i, p in enumerate(progresses):
        if (100 - p) % speeds[i]:
            takes_days.append((100 - p) // speeds[i] + 1)
        else:
            takes_days.append((100 - p) // speeds[i])
    
    for t in takes_days:
        if takes_days[0] >= t:
            cnt += 1
        else:
            answer.append(cnt)
            takes_days[0] = t
            cnt = 1
    answer.append(cnt)
    return answer

# 방법2
def solution(progresses, speeds):
    takes_days = []
    li = []
    answer = []
    cnt = 0
    
    for i, p in enumerate(progresses):
        if (100 - p) % speeds[i]:
            takes_days.append((100 - p) // speeds[i] + 1)
        else:
            takes_days.append((100 - p) // speeds[i])
            
    for t in takes_days:
        if li == []:
            li.append(t)
            cnt += 1
        elif li[0] >= t:
            cnt += 1
        else:
            answer.append(cnt)
            li = [t]
            cnt = 1
    answer.append(cnt)
    return answer

# 방법3
from collections import deque
def solution(progresses, speeds):
    takes_days = deque()
    answer = []
    cnt = 1
    
    for i, p in enumerate(progresses):
        if (100 - p) % speeds[i]:
            takes_days.append((100 - p) // speeds[i] + 1)
        else:
            takes_days.append((100 - p) // speeds[i])
        try:
            if takes_days[0] >= takes_days[1]:
                takes_days.pop()
                cnt += 1
            else:
                answer.append(cnt)
                takes_days.popleft()
                cnt = 1
        except:
            pass
    
    answer.append(cnt)
    return answer