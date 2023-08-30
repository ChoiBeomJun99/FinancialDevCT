#알고리즘(노말)_크기가작은부분문자열
#%%
def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        if(t[i:i+len(p)]<=p):
            answer+=1
    return answer