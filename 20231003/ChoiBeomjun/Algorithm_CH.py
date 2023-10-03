# 연속된 부분 수열을 구하고 k와 합을 비교한다.
# 가장 수가 적고, (idx)가 앞쪽인 수열을 찾으면 된다.)

def solution(sequence, k):
    answer = []
    
    left = 0
    right = -1
    nowSum = 0
    
    while True:         
        if nowSum < k:
            #현재 합이 더 작은 경우 (우측거를 하나 증가)
            right += 1
            if right >= len(sequence):
                break
            nowSum += sequence[right]
        else:
            #현재 합이 더 큰 경우 (왼쪽거를 하나 증가)
            nowSum -= sequence[left]
            if left + 1 >= len(sequence):
                break
            left += 1
            
        if nowSum == k:
            answer.append([left, right])
            
    tmp = sorted(answer, key = lambda x:(x[1] - x[0]))
    return tmp[0]