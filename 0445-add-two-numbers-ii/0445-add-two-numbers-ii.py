class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2 = [],[]
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        n1,n2 = "".join(n1), "".join(n2)
        ans = [int(x) for x in str(int(n1) + int(n2))]
        head = headCopy = ListNode(0)
        for n in ans:
            head.next = ListNode(n)
            head  = head.next
        return headCopy.next