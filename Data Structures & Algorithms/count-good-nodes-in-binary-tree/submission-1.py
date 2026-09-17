# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root, root.val)
        
    def helper(self, root, max_val):
        if not root:
            return 0
        
        result = 1 if root.val >= max_val else 0
        if root.val > max_val:
            max_val = root.val
        result += self.helper(root.left,max_val)
        result += self.helper(root.right,max_val)
        return result
            
        



        
        