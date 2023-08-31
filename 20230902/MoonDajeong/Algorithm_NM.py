# %%
#알고리즘(NM)
numbers = [2,1,3,4,1]
answer = []
for i in range(0,len(numbers)-1):
    for j in range(i+1,len(numbers)):
        num = numbers[i]+numbers[j]
        if(answer.count(num)==0):
            answer.append(num)
answer.sort()  #원본에 정렬 결과를 저장
print(answer)

#(1)원래 처음에는 new = answer.sort() 일케 결과 할당해줬는데, 원본에 결과가 저장되는 거라 null 결과
#(2)디폴트 오름차순(리스트.sort(reverse=False)), 내림차순(리스트.sort(reverse=True))