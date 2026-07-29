import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for _ in range(n)]
        for i in range(n):
            x1,y1 = points[i][0],points[i][1]
            for j in range(n):
                if i!=j:
                    x2,y2 = points[j][0],points[j][1]
                    cost = abs(x1-x2)+abs(y1-y2)
                    adj[i].append((j,cost))
                    adj[j].append((i,cost))
        pq = []
        visited = [0]*n
        cost = 0
        heapq.heappush(pq,(0,0,-1))
        while pq:
            wei,node,par = heapq.heappop(pq)
            if visited[node]:
                continue 
            cost+=wei
            visited[node] = 1
            for nei,neiwei in adj[node]:
                if visited[nei]!=1:
                    heapq.heappush(pq,(neiwei,nei,node))
        return cost