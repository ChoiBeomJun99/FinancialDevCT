def solution(numbers):
    answer = []
    numbers_bin = []

    for number in numbers:
        numbers_bin = list("0" + bin(number)[2:])
        idx = "".join(numbers_bin).rfind("0")
        numbers_bin[idx] = "1"

        if number % 2 != 0:  # 홀수라면
            numbers_bin[idx + 1] = "0"

        answer.append(int("".join(numbers_bin), 2))

        # int(인자,2) => 2진수를 10진수로 변환해줌

    return answer
