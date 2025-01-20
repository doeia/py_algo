def find_sum_of_three(nums, target):
    nums.sort()

    # len(nums) - 2 是用于限制外层 for 循环的迭代范围，以确保我们始终有足够的数字来组成一个三元组（nums[i] + nums[low] + nums[high]）。
    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        # 重点：怎么让数据相向移动
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True
            elif triplet < target:
                low += 1
            else:
                high -= 1
    return False
