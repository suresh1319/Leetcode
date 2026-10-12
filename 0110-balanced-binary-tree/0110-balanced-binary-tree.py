# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        isBalanced = True
        def check(node):
            nonlocal isBalanced
            if node is None:
                return 0
            if not isBalanced:
                return 0 
            lh = check(node.left)
            rh = check(node.right)
            if abs(lh-rh)>1:
                isBalanced = False 
                return 0
            return 1+max(lh,rh)
        k = check(root)
        return isBalanced

        