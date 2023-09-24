from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    limit = len(queue1) * 4 # greedy의 경우 (최악의 경우를 선정 -> queue1, queue2가 서로 바뀌고 또 바뀌어서 서로 다시 원상태로 돌아가는 경우의 수)
    
    while True:
        if answer >= limit: # 다시 원상태로 복구 되는 경우 (결국 서로의 합은 만족 못함.)
            answer = -1
            break
        
        # 합이 높은 쪽에서 빼서 낮은 쪽에 더한다.
        if sum1 > sum2:
            tmp = queue1.popleft()
            sum1 -= tmp
                
            queue2.append(tmp)
            sum2 += tmp
            
            answer += 1 # 추출 후 다른 큐에 넣어줬으므로 횟수 += 1 해준다.
        
        elif sum1 < sum2:
            tmp = queue2.popleft()
            sum2 -= tmp
            
            queue1.append(tmp)
            sum1 += tmp
            
            answer += 1 # 추출 후 다른 큐에 넣어줬으므로 횟수 += 1 해준다.
                
        if sum1 == sum2:
            break
    
    return answer