# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False 
        if root and not subRoot:
            return True

        if self.subTree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot)) or self.isSubtree(root.right, subRoot)

    def subTree(self, r, t):
        if not r and not t:
            return True
        if r and t and r.val == t.val:
            return (self.subTree(r.left,t.left)) and (self.subTree(r.right,t.right))
        