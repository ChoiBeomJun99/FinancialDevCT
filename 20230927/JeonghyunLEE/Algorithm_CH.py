# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque
def solution(queue1, queue2):
    cnt = 0
    limit = len(queue1) * 3
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    while cnt < limit:
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            q2.append(q1.popleft())
        elif sum1 < sum2:
            sum1 += q2[0]
            sum2 -= q2[0]
            q1.append(q2.popleft())
        else:
            return cnt
        cnt +=1
    return -1