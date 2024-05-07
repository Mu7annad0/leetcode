# You are given the head of a linked list.
#
# Remove every node which has a node with a greater value anywhere to the right side of it.
#
# Return the head of the modified linked list.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):

            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
            return prev

        head = reverse(head)
        curr = head
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next
        return reverse(head)


# Create the ListNode for [1, 8, 9]
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

# Execute the function with the created ListNode
solution = Solution()
result = solution.removeNodes(head)

# Print the result
current = result
while current is not None:
    print(current.val)
    current = current.next

# 13
# 8
