def solution(n, m):
    answer = []
    
    #range(start, stop, step)
    #range() 함수의 결과는 반복가능(iterable)하기 때문에 for문을 사용해 출력할 수 있음
    for i in range(min(n, m), 0, -1):
        #n,m 최소에서 시작, 0에서 stop, -1씩 스텝
        if((n % i == 0) and (m % i == 0)) :
            answer.append(i)            
            break
    
    for i in range(max(n,m), n*m+1):
        if((i%n==0) and (i%m==0)):
            answer.append(i)
            break
        
    return answer