#알고리즘(NM)_숫자문자열과 영단어
#%%
def solution(s):
    num = [0,1,2,3,4,5,6,7,8,9]
    word = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(0, len(num)):
        if(word[i] in s):
            s = s.replace(word[i], str(num[i]))
    return int(s)

#주의할점
#(1) 마지막 출력값은 숫자 >> int() 쓰기...
#(2) replace 함수... OO이 존재하면 OO을 모두 바꿔줌