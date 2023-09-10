def solution(arr1, arr2):
    a, b, m, n = len(arr1), len(arr2[0]), 0, 0
    answer = [[i for i in range(b)] for j in range(a)]
    while m < a:
        tmp = 0
        for i in range(len(arr2)):
            tmp += arr1[m][i] * arr2[i][n]
        answer[m][n], tmp, m, n = tmp, 0, (m + 1) if n == b - 1 else m, (n + 1) if n < b - 1 else 0
    return answer
