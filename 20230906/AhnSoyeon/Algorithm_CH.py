import re

def string_split(s):
    s = s.lower()
    head= re.match('[\D]+',s)
    number = re.search('[0-9]+',s)
    file = [head[0], int(number[0]), s[number.end():]]
    return file

def solution(files):
    new_files = []
    for i, file in enumerate(files):
        s_file = string_split(file.lower())
        s_file.append(i)
        new_files.append(s_file)
    new_files.sort(key = lambda x : (x[0], x[1], x[-1]))
    answer = list(map(lambda x : files[x[-1]], new_files))
    return answer
