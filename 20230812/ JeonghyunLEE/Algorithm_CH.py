# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    c_dict = {}
    
    for c_name, c_type in clothes:
        try:
            c_dict[c_type].append(c_name)
        except:
            c_dict[c_type] = [c_name]
    
    for c in c_dict.values():
        answer *= len(c) + 1
    
    return answer - 1