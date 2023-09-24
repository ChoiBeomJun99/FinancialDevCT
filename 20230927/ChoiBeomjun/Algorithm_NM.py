# 이진수로 바꾼 뒤 해석하기
def toBinary(n, arr):
    result = []
    
    for i in arr:
        tmp = list(bin(i)[2:])
        
        while len(tmp) < n:
            tmp.insert(0, 0)
            
        result.append(tmp)

    return result
        

def solution(n, arr1, arr2):
    answer = []
    
    fir_map = toBinary(n, arr1) # 첫 번째 지도
    sec_map = toBinary(n, arr2) # 두 번째 지도
    
    for i in range(n):
        tmp = ""
        for j in range(n):
            if int(fir_map[i][j]) + int(sec_map[i][j]) > 0:
                # 벽인 부분
                tmp += '#'
            else:
                # 공백인 부분
                tmp += ' '
                
        answer.append(tmp)
            
    return answer