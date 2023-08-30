#%%
import pandas as pd

# %%
#알고리즘(챌린지)

want = ['banana','apple','rice','pork']
number = [3,1,2,2]
discount = ['chicken','apple','apple','banana','rice','apple','pork','banana','pork','rice','pot','banana','apple','banana']
answer = 0
for i in range(0,len(discount)-9):
    what = discount[i:i+10]
    res = 0
    for j in range(0,len(number)):
        if(what.count(want[j])>=number[j]):
            res += 1
    if(res==len(number)):
        answer += 1
print(answer)
#%%
for i in range(0,1):
    print(i)
# %%
