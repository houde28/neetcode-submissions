# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root,float('inf'),float('-inf'))

    def dfs(self, root, upper,lower):
        if not root:
            return True
        
        if root.val > lower and root.val < upper:
            left = self.dfs(root.left,root.val,lower)
            right = self.dfs(root.right,upper,root.val)
            return True and left and right
        else:
            return False
        
