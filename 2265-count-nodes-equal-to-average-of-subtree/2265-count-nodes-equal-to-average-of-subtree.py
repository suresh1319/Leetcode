# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 
        ans = 0
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0,0 
            leftSum,leftCnt = dfs(node.left)
            rightSum,rightCnt = dfs(node.right) 
            summ = leftSum+rightSum+node.val
            cnt = leftCnt+rightCnt+1
            if summ//cnt == node.val:
                ans += 1
            return summ,cnt
        dfs(root)
        return ans

        