# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy= ListNode(next =head)
        prevGroup=dummy
        while True:
            kth = self.getkth(prevGroup, k)
            if not kth:
                break
            nextkgroup = kth.next
            prev, curr = kth.next, prevGroup.next

            while curr != nextkgroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
                
        return dummy.next
        
    def getkth(self,prevGroup,k):
        curr = prevGroup
        while curr and k > 0:
            k -= 1
            curr = curr.next

        return curr

