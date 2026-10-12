# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxPath = float('-inf')
        def calSum(node):
            nonlocal maxPath
            if node is None:
                return 0
            ls = max(calSum(node.left),0)
            rs = max(calSum(node.right),0)
            maxPath = max(maxPath,node.val+ls+rs)
            return node.val+max(ls,rs)
        calSum(root)
        return maxPath
