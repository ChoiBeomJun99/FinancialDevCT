def solution(clothes):
    # 아이디어 제시 "얼굴"에 착용할 의상이 2가지 있다면 3으로 취한다 (아무것도 없는 경우 포함)
    # 하지만 모든 "종류"에 해당하는 모든 부위를 안입는 경우는 제외하므로 이 경우는 배제해야한다. 곱한 값에서 -1
    
    
    # 1.리스트 메소드 사용한 방식
#     types = [] # 종류가 들어갈 값
#     countOfType = [] # 종류마다 의상 개수를 저장
    
#     for i in clothes:
#         if i[1] in types:
#             idx = types.index(i[1])
#             countOfType[idx] += 1
#         else:
#             types.append(i[1])
#             countOfType.append(1)
            
#     answer = 1
#     for i in countOfType:
#         answer *= i + 1
        
        
    # 2. Dict 사용한 방식 (이게 더 효율적!)
    dic = {}
    
    for i in clothes:
        dic[hash(i[1])] = dic.get(hash(i[1]), 0) + 1
    
    answer = 1
    for i in dic:
        answer *= dic[i] + 1

    
    return answer - 1