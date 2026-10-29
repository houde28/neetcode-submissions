"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        completed = {}

        def helper(clone):
            if clone in completed:
                return completed[clone]
            
            copy = Node(clone.val)
            completed[clone] = copy
            for nodes in clone.neighbors:
                copy.neighbors.append(helper(nodes))
            return copy
        return helper(node)
