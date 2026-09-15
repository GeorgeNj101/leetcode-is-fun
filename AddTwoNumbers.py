from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        s1 = ""
        s2 = ""
        while head1 is not None or head2 is not None:
            s1 += str(head1.val) if head1 is not None else ""
            
            s2 += str(head2.val) if head2 is not None else ""

            if head1 is not None:
                head1 = head1.next

            if head2 is not None:
                head2 = head2.next
        
        ans = str(int(s1[::-1]) + int(s2[::-1]))
        ans = ans[::-1]

        head = ListNode(int(ans[0]))
        current = head
        for char in ans[1:]:
            current.next = ListNode(int(char))
            current = current.next
        return head