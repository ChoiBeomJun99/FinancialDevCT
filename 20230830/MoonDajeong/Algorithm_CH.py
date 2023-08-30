#알고리즘(챌린지)_할인행사
def solution(want, number, discount):
    answer=0
    #for문 range() 지정에서 오류발생했엇음...문제잘읽기ㅠ_ㅠ
    for i in range(0,len(discount)-9):
        what = discount[i:i+10]
        res = 0
        for j in range(0,len(number)):
            if(what.count(want[j])>=number[j]):
                res += 1
        if(res==len(number)):
            answer += 1
    return answer