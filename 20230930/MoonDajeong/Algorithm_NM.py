#알고리즘(노말)_문자열내맘대로정렬하기

#%%
def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x : x[n])
    return strings