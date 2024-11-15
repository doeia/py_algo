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


def traverse(root):
    if root is None:
        return 0
    # 递归计算左右子树的节点数

    print('leftCount', traverse(root.left))
    # leftCount = traverse(root.left)
    rightCount = traverse(root.right)
    # 当前节点的总数 = 左子树节点数 + 右子树节点数 + 当前节点（root）
    return rightCount + 1


# Test the Solution class
if __name__ == "__main__":
    arr = ['a', 'b', 'c', 'd', 5, 6, 7]
    root = build_tree(arr)
    print("Original tree level order traversal:")
    print(traverse(root))
