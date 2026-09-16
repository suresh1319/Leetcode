# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        def kSumPath(root,res,mp,summ):
            if root is None:
                return 
            summ+=root.val 
            res[0]=res[0]+mp.get(summ-k,0)
            mp[summ] = mp.get(summ,0)+1
            kSumPath(root.left,res,mp,summ)
            kSumPath(root.right,res,mp,summ)
            mp[summ] = mp[summ]-1
        mp = {0:1}
        res = [0]
        kSumPath(root,res,mp,0)
        return res[0]