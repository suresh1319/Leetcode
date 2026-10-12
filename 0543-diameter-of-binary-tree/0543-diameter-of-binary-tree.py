# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = float('-inf')
        def traverse(node):
            nonlocal maxDia
            if node is None:
                return 0 
            lh = traverse(node.left)
            rh = traverse(node.right)
            maxDia = max(maxDia,1+lh+rh)
            return 1+max(lh,rh)
        traverse(root)
        return maxDia-1
