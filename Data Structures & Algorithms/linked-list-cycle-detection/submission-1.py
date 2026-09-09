# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head 
        fast = head.next
        
        while slow != fast:
            if slow.next is None or fast.next is None or fast.next.next is None:
                return False
            slow=slow.next
            fast=fast.next.next


        return True
