from collections import deque 

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1) 
    sum2 = sum(q2)
    
    total = sum1 +sum2
    
    if total % 2 != 0: # 전체 합이 홀수일때
        return -1
    
    # 반복 횟수는 큐 길이 * 3 
    while answer <= len(queue1)*3:
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1 -= q2[-1]
            sum2 += q2[-1]
            answer += 1
        elif sum1 < sum2:
            q1.append(q2.popleft())
            sum1 += q1[-1]
            sum2 -= q1[-1]
            answer += 1
        else:
            return answer
    return -1