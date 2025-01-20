def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        # 슬라이싱 후 정렬하고, k번째 원소 반환
        sliced_array = sorted(array[i-1:j])
        result.append(sliced_array[k-1])
    return result


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)
