def solution(skill, skill_trees):
    answer = 0
    onlySkill = []
    
    # 스킬 트리 내 필요없는 것들은 빼주기
    for value in skill_trees:
        tmp = list(value)
        save = [j for j in tmp]
        for s in tmp:
            if s not in skill:
                save.remove(s)
        
        onlySkill.append(save)
                
    # 본격 순서 비교
    for i in onlySkill:
        comSkill = list(skill)
        tmp = 1
        for j in i:
            if j in comSkill:
                if comSkill.index(j) == 0:
                    comSkill.pop(0)
                else:
                    tmp = 0
                    break
            else:
                tmp = 0
                continue

        if tmp == 1:
            answer +=1
        
    return answer