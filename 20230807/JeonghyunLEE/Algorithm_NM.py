# https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 방법 1
def solution(s):
    if len(s) == 4 or len(s) ==6:
        return s.isnumeric()
    else:
        return False
    
# 방법 2
def solution(s):
    number = [i for i in range(10)]
    if len(s) != 4 and len(s) != 6:
        return False
    
    for string in list(s):
        try:
            int(string)
        except:
            return False
    return True