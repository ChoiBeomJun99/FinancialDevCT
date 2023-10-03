def solution(dartResult):
    scores = []
    current_score = ""

    for char in dartResult:
        if char.isdigit():
            current_score += char
        elif char == "S":
            scores.append(int(current_score))
            current_score = ""
        elif char == "D":
            scores.append(int(current_score) ** 2)
            current_score = ""
        elif char == "T":
            scores.append(int(current_score) ** 3)
            current_score = ""
        elif char == "*":
            if len(scores) >= 2:
                scores[-2] *= 2
            scores[-1] *= 2
        elif char == "#":
            scores[-1] *= -1

    return sum(scores)
