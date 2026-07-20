# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root 
        node = TreeNode(val)
        if root is None:
            return node
        prev = None 
        while temp:
            if temp.val>=val:
                prev = temp
                temp = temp.left 
            else:
                prev = temp
                temp = temp.right 
        if prev.val>val:
            prev.left = node 
        else:
            prev.right = node 
        return root