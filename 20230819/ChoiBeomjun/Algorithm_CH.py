from collections import Counter

def refineArr(strArr):
    result = []
    
    for i, v in enumerate(strArr):
        if i < len(strArr) - 1:
            # 특수문자 포함 여부 검사
            if str(v).isalpha() and str(strArr[i+1]).isalpha():
                result.append(str(v).lower() + str(strArr[i+1]).lower())
                
    return result

def solution(str1, str2):                          
    answer = 0
        
    # 다중 집합 원소로 만들기 (전처리 과정)
    refine1 = refineArr(str1)
    refine2 = refineArr(str2)
    
    # 둘 다 공집합인 경우
    if len(refine1) == 0 and len(refine2) == 0:
        return 65536

    # Counter 가 포인트 입니다. 각 원소가 Key, 개수가 Value로 들어갑니다. 
    refine1 = Counter(refine1)
    refine2 = Counter(refine2)
        
    # 교집합 구하기
    gyo = list((refine1 & refine2).elements())
    
    # 합집합 구하기
    hap = list((refine1 | refine2).elements())
                              

    return int(len(gyo) / len(hap) * 65536)