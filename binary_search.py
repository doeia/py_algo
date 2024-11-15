from typing import List


def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums) - 1

    while left <= right:
        # 直接使用 (right + left) // 2 也可能会导致整数溢出问题
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 注意
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid - 1


def bs(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    result = binarySearch(nums, target)
    print(f"目标值的索引: {result}")
