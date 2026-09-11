"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        dictionary = {None: None}
        while current is not None:
            copy = Node(current.val)
            dictionary[current] = copy
            current = current.next
        current = head
        while current is not None:
            copy = dictionary[current]
            copy.next = dictionary[current.next]
            copy.random = dictionary[current.random]
            current = current.next

        return dictionary[head]