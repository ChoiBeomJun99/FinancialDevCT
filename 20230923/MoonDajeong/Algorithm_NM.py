#알고리즘(노말)_예산
#%%
import numpy as np

# %%
#최대한많은부서에 물품나눠주기
#신청한 만큼은 반드시 지원해줘야됨
#최대 몇개부서에 물품지원가능?
#걍정렬해서 작은거부터 세어나가면되는거아님?

#런타임에러발생.... 왜....왜...왜....
def solution(d, budget):
    d.sort()
    money, i= 0,0
    while True:
        money += d[i]
        i += 1
        if(money == budget):
            break
        elif(money > budget):
            i -= 1
            break
    return i
