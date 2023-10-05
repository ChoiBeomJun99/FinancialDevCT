def solution(sequence, k):
    answer = []
    start = 0 
    end = 0
    num = sequence[0] #sequence의 첫 값 저장
    min_len = 99999999999 #임의의 큰 값 저장
    
    while start <= end and end < len(sequence):
        if num == k:
            if min_len > end - start + 1:
                min_len = end - start + 1
                answer = [start, end]
            num -= sequence[start]
            start += 1

        elif num > k:
            num -= sequence[start]
            start += 1
        
        elif num < k:
            end+=1
            if end < len(sequence):
                num += sequence[end]
        
    return answer