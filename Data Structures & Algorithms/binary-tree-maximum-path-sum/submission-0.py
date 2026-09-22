# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def helper(root):
            if not root:
                return 0
            leftmax=helper(root.left)
            rightmax=helper(root.right)
            leftmax= max(leftmax, 0)
            rightmax = max(rightmax, 0)
            res[0] = max(res[0],root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax)
        helper(root)
        return res[0]
