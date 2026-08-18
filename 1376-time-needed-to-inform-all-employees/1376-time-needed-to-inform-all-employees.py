from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)
        def bfs(node):
            dq = deque()
            dq.append((node,0))
            ans = 0
            max_time = 0
            visited = [0]*n 
            while dq:
                curr,time = dq.popleft()
                max_time = max(max_time,time)
                for nei in adj[curr]:
                    dq.append((nei,time+informTime[curr]))
            return max_time
        return bfs(headID)