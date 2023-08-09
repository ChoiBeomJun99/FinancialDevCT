# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 방법 1
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

# 방법 2
from collections import deque
def solution(progresses, speeds):
    takes_days = []
    que = deque()
    answer = []
    cnt = 0
    
    for i, p in enumerate(progresses):
        if (100 - p) % speeds[i]:
            takes_days.append((100 - p) // speeds[i] + 1)
        else:
            takes_days.append((100 - p) // speeds[i])
            
    for t in takes_days:
        if que == deque():
            que.append(t)
            cnt += 1
        elif que[0] >= t:
            cnt += 1
        else:
            answer.append(cnt)
            que = deque([t])
            cnt = 1
    answer.append(cnt)
    
    return answer