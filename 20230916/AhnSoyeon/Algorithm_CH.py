def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        mytree = ''.join([str1 for str1 in tree if str1 in skill])
        if skill.startswith(mytree):
            answer+=1
    return answer
