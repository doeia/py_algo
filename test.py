from collections import deque


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(arr):
    if not arr:
        return None

    index = 0
    root = BinaryTreeNode(arr[index])
    index += 1
    queue = deque([root])

    while index < len(arr):
        node = queue.popleft()
        item = arr[index]
        index += 1
        if item is not None:
            node.left = BinaryTreeNode(item)
            queue.append(node.left)
        if index >= len(arr):
            break
        item = arr[index]
        index += 1
        if item is not None:
            node.right = BinaryTreeNode(item)
            queue.append(node.right)

    return root


def print_tree(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


class Solution:
    # 主函数
    def invertTree(self, root):
        # 遍历二叉树，交换每个节点的子节点
        self.traverse(root)
        return root

    # 二叉树遍历函数
    def traverse(self, root):
        if not root:
            return

        # *** 前序位置 ***
        # 每一个节点需要做的事就是交换它的左右子节点
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # 遍历框架，去遍历左右子树的节点
        self.traverse(root.left)
        self.traverse(root.right)


# Test the Solution class
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(arr)
    print("Original tree level order traversal:")
    print_tree(root)

    solution = Solution()
    inverted_root = solution.invertTree(root)
    print("Inverted tree level order traversal:")
    print_tree(inverted_root)
