class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if node is None:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                tempRi = node.right 
                node.right = node.left 
                node.left = None 
                left.right = tempRi 
            if right:
                return right 
            if left:
                return left 
            return node 
        return dfs(root)



