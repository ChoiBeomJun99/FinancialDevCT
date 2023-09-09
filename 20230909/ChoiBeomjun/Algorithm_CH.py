def solution(arr1, arr2):
    # [a,b] * [b,c] = [a,c] 행렬에서 a, b, c 구하기
    a = len(arr1)
    b = len(arr2)
    c = len(arr2[0])
    
    # answer - 2차원 배열 모든 idx 자리 0으로 초기화
    answer = [[0] * c for _ in range(a)]
    
    for i in range(a): 
        lists = []
        for j in range(c): 
            for k in range(b): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
            
    return answer