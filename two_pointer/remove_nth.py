# Definition for a Linked List node
from linked_list import LinkedList


class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_nth_last_node(head, n):
    right = head
    left = head

    # 重点：怎么让数据移动
    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    # 重点：怎么让数据移动
    while right.next:
        # 这里移动right, 是为了让while判断right 到哪了
        right = right.next
        left = left.next

    left.next = left.next.next

    return head
