def solution(d, budget):
    answer = 0
    
    for i in sorted(d):
        budget -= i
        if budget < 0: 
            break
        answer += 1
        
    return answer

'''
sorted 함수는 파이썬 내장 함수입니다.
첫 번째 매개변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어서 반환해 주는 함수입니다.
'''