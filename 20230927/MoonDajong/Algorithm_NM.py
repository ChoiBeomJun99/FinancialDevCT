#알고리즘(노말)_[1차]비밀지도
#1. 공백( )과 벽(#, 1)
#2. 둘 중 하나라도 벽이면 벽, or
#풀이시간 : 14분

# def solution(n, arr1, arr2):
#     maxnum = len(bin(max(arr1+arr2))[2:])

#     for i in range(0,n):
#         arr1[i] = bin(arr1[i])[2:]
#         arr2[i] = bin(arr2[i])[2:]
#         if(len(arr1[i])!=maxnum):
#             arr1[i] = '0'*(maxnum-len(arr1[i]))+arr1[i]
#         if(len(arr2[i])!=maxnum):
#             arr2[i] = '0'*(maxnum-len(arr2[i]))+arr2[i]

#     res = []
#     word = ''
#     for i in range(0,n):
#         word = ''
#         for j in range(0,maxnum):
#             if((arr1[i][j]=='0')&(arr2[i][j]=='0')):
#                 word += ' '
#             else:
#                 word += '#'
#         res.append(word)

#     return res
# %%
n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
#1. 최대 이진수 자리수 찾기
maxnum = len(bin(max(arr1+arr2))[2:])

#2. 각각 이진수로 변경완료
for i in range(0,n):
    arr1[i] = bin(arr1[i])[2:]
    arr2[i] = bin(arr2[i])[2:]
    if(len(arr1[i])!=maxnum):
        arr1[i] = '0'*(maxnum-len(arr1[i]))+arr1[i]
    if(len(arr2[i])!=maxnum):
        arr2[i] = '0'*(maxnum-len(arr2[i]))+arr2[i]

#3. 최종 출력값
res = []
word = ''
for i in range(0,n):
    word = ''
    for j in range(0,maxnum):
        if((arr1[i][j]=='0')&(arr2[i][j]=='0')):
            word += ' '
        else:
            word += '#'
    res.append(word)
print(res)

#몰랐던점
#1. 10진수를 2진수로 바꾸는 함수 : bin
# %%
