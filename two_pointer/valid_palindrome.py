def is_palindrome_wrong(s):
    low = 0
    high = len(s) - 1
    for x in range(s):
        if s[low] is not s[high]:
            return False
        low + 1
        high - 1
    return True


def is_palindrome_right(s):
    left = 0
    # 要挪一步索引
    right = len(s) - 1
    # 重点：怎么让数据移动到一半
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True
