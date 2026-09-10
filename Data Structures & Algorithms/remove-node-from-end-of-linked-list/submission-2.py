# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=head
        index = 0
        while index != n:
            if first is not None:
                first=first.next
                index += 1
        second = ListNode(next = head)
        second_dummy = second
        while first is not None:
            print("first: ", first.val, "second: ", second.val)
            first=first.next
            second=second.next
        
        second.next= second.next.next
        
        return second_dummy.next
        

        