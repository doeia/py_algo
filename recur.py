def count_array(arr, index=0):
    if index >= len(arr):
        return 0
    print(count_array(arr, index + 1))  # 递归处理下一个元素


# 数组示例
arr = [1, 2, 3, 4, 5]
count_array(arr)
