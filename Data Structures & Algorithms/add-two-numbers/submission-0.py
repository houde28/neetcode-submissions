# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy
        
        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2 is not None:
                l2_val = l2.val
            else:
                l2_val = 0

            summ = l1_val + l2_val + carry
            digit = summ % 10
            carry = summ // 10
            current.next=ListNode(digit)
            current = current.next
            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
        
        if carry == 1:
            current.next = ListNode(val=carry)

        return dummy.next
            

        