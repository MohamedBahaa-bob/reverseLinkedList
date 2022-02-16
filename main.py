# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    input = [1, 2, 3, 4, 5]
    node = ListNode(input[0])
    root = node
    for i in range(1, len(input)):
        node.next = ListNode(input[i])
        node = node.next

    result = obj.reverseList(root)
    # print(result.val)
    while result is not None:
        print(result.val)
        result = result.next

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
