from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
            return prev

        head, prev = reverse(head), None
        curr = head
        carry = 0
        while curr:
            doubled_val = (curr.val * 2) + carry
            curr.val = doubled_val % 10
            carry = doubled_val // 10
            prev, curr = curr, curr.next
        if carry:
            prev.next = ListNode(carry)

        curr = reverse(head)
        return curr


# another solution but not the best one
class Solution2:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        the_numbers = []
        curr = head
        while curr:
            the_numbers.append(curr.val)
            curr = curr.next

        doubled_integer = 2 * int(''.join(map(str, the_numbers)))
        doubled_list = [int(d) for d in str(doubled_integer)]

        head = ListNode(doubled_list[0])
        curr = head
        for item in doubled_list[1:]:
            curr.next = ListNode(item)
            curr = curr.next

        return head


# Create the ListNode for [1, 8, 9]
head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(9)

# Execute the function with the created ListNode
solution = Solution()
result = solution.doubleIt(head)

# Print the result
current = result
while current is not None:
    print(current.val)
    current = current.next

# 3
# 7
# 8
