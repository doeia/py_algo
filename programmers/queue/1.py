def solution(arr):
    # 결과를 저장할 리스트
    result = []

    # 배열을 순차적으로 탐색
    for num in arr:
        # result가 비어있거나, 이전 값과 다른 숫자가 나오면 추가
        if not result or result[-1] != num:
            result.append(num)

    return result
