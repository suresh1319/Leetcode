class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n == 0:
            return None 
        if n == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 1
        while i<n and preorder[0]>preorder[i]:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
