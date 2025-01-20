from functools import cmp_to_key


def solution(numbers):
    # 비교 함수 정의
    def compare(a, b):
        # a + b가 b + a보다 크면 a가 앞에 오도록
        if a + b > b + a:
            return -1  # a가 b보다 우선
        elif a + b < b + a:
            return 1   # b가 a보다 우선
        else:
            return 0   # 같으면 상관없음

    # 숫자 배열을 문자열로 변환하고, 비교 기준에 맞게 정렬
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))

    # 정렬된 숫자들을 합친 후, 0으로만 이루어진 경우 처리
    result = ''.join(numbers)
    if result[0] == '0':
        return '0'

    return result
