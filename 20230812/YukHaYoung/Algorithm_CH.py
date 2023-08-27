#해시 : 데이터 다루는 기법 중에 하나로 검색과 저장이 빠르게 진행
#key-value 페어 관리 딕셔너리 {Key1: Value1}
def solution(clothes):
    closet = {}
    answer = 1
    
    for cloth in clothes:
        #clothes의 각 행은 [의상의 이름, 의상의 종류]
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
            
    for cases in closet.values():
        answer *= len(cases) + 1
    
    return answer-1 #서로 다른 옷의 조합의 수를 return
