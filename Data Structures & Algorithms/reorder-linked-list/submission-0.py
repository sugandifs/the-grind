# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # when fast reaches the end, slow will be at the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # since slow is at midpoint, we cut it off so that we split
        # the list into two parts
        second = slow.next
        prev = slow.next = None

        # this is the second half, towards the right
        # we reverse this part
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # we merge the two parts
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


