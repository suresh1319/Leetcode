class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))
        visited = set([0])
        changes = 0
        def dfs(node):
            nonlocal changes
            visited.add(node)
            for nei,cost in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    changes += cost 
                    dfs(nei)
        dfs(0)
        return changes
        