# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        dq = deque()
        if root is None:
            return ans
        dq.append(root)
        while dq:
            n = len(dq)
            temp = []
            for _ in range(n):
                ele = dq.popleft()
                temp.append(ele.val)
                if ele.left:
                    dq.append(ele.left)
                if ele.right:
                    dq.append(ele.right)
            ans.append(temp.pop())
        return ans

