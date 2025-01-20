# 输入一棵二叉树的根节点，层序遍历这棵二叉树
from typing import List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            tmp = []
            for i in range(size):
                cur = q.popleft()
                tmp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp)
        return res


# Create a larger binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#   / \   \
#  7   8   9
#     / \
#    10  11

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)
root.left.right.right = TreeNode(9)
root.left.left.right.left = TreeNode(10)
root.left.left.right.right = TreeNode(11)


# Create an instance of Solution and call levelOrder
solution = Solution()
result = solution.levelOrder(root)
print(result)  # Output: [[1], [2, 3], [4, 5, 6]]
