class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]+dist[k][j]<dist[i][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
        ans = 0
        all_min = float('inf')
        for i in range(n):
            min_cities = 0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    min_cities += 1
            if min_cities<=all_min:
                all_min = min_cities
                ans = i 
        return ans