def solution(arr1, arr2):
    # 더하는 두 행렬의 행, 열 개수 구하기
    m = len(arr1)
    n = len(arr1[0])

    answer = [[0] * n for _ in range(m)]
    
    for i in range(0, m):
        for j in range(0, n):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer