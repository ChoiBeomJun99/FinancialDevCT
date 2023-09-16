#알고리즘(노말)_푸드파이트대회
#%%
#(1) 칼로리가 낮은 음식부터 먹게
#(2) 걍 food 순서대로 가져와서 1인지판단 후 짝홀 판단
#(3) 
#(4) 리스트 돌아가는거 다끝나면 0
#(5) 0 기준 앞에껄 반대로해서 붙이기
def solution(food):
    answer = ''
    #먹을수있는음식의순서번호가 아니라, 걍 그음식의번호..
    for i in range(0, len(food)):
        if(food[i]!=1):
            answer += (str(i)*(food[i]//2))
            #으잉근데 왜 str(i)이면 되는거지 str(i+1) 이어야하는거아닝가..
        else:
            pass
    answer += ('0'+answer[::-1]) 
    return answer


