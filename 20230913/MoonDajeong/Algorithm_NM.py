#알고리즘(노말)_행렬의덧셈
#%%
#틀린답 -- 애초에 행렬이 list로 배열이 아니라 리스트로 받아와짐..
# def solution(arr1, arr2):
#     for i in range(0,arr1.shape[0]):
#         for j in range(0,arr2.shape[1]):
#             arr1[i,j] = arr1[i,j]+arr2[i,j]
#     return arr1

def solution(arr1, arr2):
    for i in range(0,len(arr1)):
        for j in range(0,len(arr1[i])):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    return arr1
