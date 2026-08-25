class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        def backtrack(ind):
            if ind >= n or ind < 0:
                return False
            if ind in visited:
                return False 
            if arr[ind] == 0:
                return True
            visited.add(ind)  
            return backtrack(ind+arr[ind]) or backtrack(ind - arr[ind])
        return backtrack(start)
