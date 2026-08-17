from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        visited = [[0,0] for _ in range(n)]
        ans = [-1]*n
        ans[0] = 0
        dq = deque()
        dq.append((0,0,0))
        dq.append((0,1,0))
        visited[0][0],visited[0][1] = 1,1
        while dq:
            node,col,dist = dq.popleft()
            if col == 0:
                for nei in blue[node]:
                    if visited[nei][1] == 0:
                        visited[nei][1] = 1
                        dq.append((nei,1,dist+1))
                        if ans[nei] == -1:
                            ans[nei] = dist+1
            else:
                for nei in red[node]:
                    if visited[nei][0] == 0:
                        visited[nei][0] = 1 
                        dq.append((nei,0,dist+1))
                        if ans[nei] == -1:
                            ans[nei] = dist+1
        return ans
                        
            