class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [0]*V
        path = [0]*V
        check = [0]*V 
        def dfs(node):
            visited[node] = 1
            path[node] = 1
            for nei in graph[node]:
                if visited[nei]!=1:
                    if dfs(nei):
                        check[nei] = 0
                        return True 
                elif path[nei] == 1:
                    check[nei] = 0
                    return True
            check[node] = 1
            path[node] = 0
            return False 
        for i in range(V):
            if visited[i]!=1:
                dfs(i) 
        ans = []
        for i in range(len(check)):
            if check[i] == 1:
                ans.append(i)
        return ans