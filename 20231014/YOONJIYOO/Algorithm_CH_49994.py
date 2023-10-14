def solution(dirs):
    answer = 0
    path = set()
    tmp = (0, 0, 0, 0)
    b_tmp = (0, 0, 0, 0)  # backwards_tmp

    for i in dirs:
        if i == "U":
            px, py, x, y = tmp
            if y < 5:
                tmp = (x, y, x, y + 1)
                b_tmp = (x, y + 1, x, y)
                path.add(tmp)
                path.add(b_tmp)

        elif i == "D":
            px, py, x, y = tmp
            if y > -5:
                tmp = (x, y, x, y - 1)
                b_tmp = (x, y - 1, x, y)
                path.add(tmp)
                path.add(b_tmp)

        elif i == "L":
            px, py, x, y = tmp
            if x > -5:
                tmp = (x, y, x - 1, y)
                b_tmp = (x - 1, y, x, y)
                path.add(tmp)
                path.add(b_tmp)

        elif i == "R":
            px, py, x, y = tmp
            if x < 5:
                tmp = (x, y, x + 1, y)
                b_tmp = (x + 1, y, x, y)
                path.add(tmp)
                path.add(b_tmp)

    answer = len(path) // 2

    return answer
