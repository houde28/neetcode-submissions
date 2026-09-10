# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        if head is None or head.next is None:
            return
        slow=head
        fast = slow.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next=None

        current = l2
        prev= None
        while current is not None:
            next_node = current.next
            current.next= prev
            prev=current
            current=next_node
        
        l2 = prev
        
        while l1 is not None and l2 is not None:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l1= next1
            l2 = next2
        return
       



        


