class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        visited = [0]*V
        color = [-1]*V
        def bfs(start):
            dq = deque()
            dq.append(start)
            visited[start] = 1
            color[start] = 0
            while dq:
                ele = dq.popleft()
                neiCol = color[ele]
                for nei in graph[ele]:
                    if visited[nei]!=1:
                        visited[nei] = 1
                        color[nei] = 0 if neiCol == 1 else 1
                        dq.append(nei)
                    elif neiCol != -1 and color[nei] == neiCol:
                        return False 
            return True 
        for i in range(V):
            if not visited[i]:
                if not bfs(i):
                    return False
        return True

