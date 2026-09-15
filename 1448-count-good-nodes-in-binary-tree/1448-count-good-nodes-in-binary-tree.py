class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,large):
            nonlocal ans
            if node is None:
                return 
            if large<=node.val:
                ans += 1
                large = node.val 
            dfs(node.left,large)
            dfs(node.right,large)
        dfs(root,float('-inf'))
        return ans