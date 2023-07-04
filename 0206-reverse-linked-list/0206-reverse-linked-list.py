# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        aaru = None
        ani = head
        while ani:
            forward = ani.next
            ani.next = aaru
            aaru = ani
            ani = forward
        return aaru