from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = [0]*n
        q = deque()
        ans = 0
        def bfs(node):
            visited[node] = 1
            q.append(node)
            while q:
                ele = q.popleft()
                for nei in adj[ele]:
                    if visited[nei] == 0:
                        visited[nei] = 1
                        q.append(nei)
        for i in range(n):
            if visited[i] != 1:
                bfs(i)
                ans +=1 
        return ans