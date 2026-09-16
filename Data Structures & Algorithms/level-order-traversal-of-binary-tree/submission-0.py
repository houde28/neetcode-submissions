# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            q_len = len(queue)
            curr_row = []
            for i in range(q_len):
                curr = queue.popleft()
                if curr:
                    curr_row.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    continue
            result.append(curr_row)
        result.pop()
        return result
