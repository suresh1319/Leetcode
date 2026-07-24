import heapq 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist = [float('inf')]*(n+1)
        heapq.heappush(pq,(0,k))
        dist[k] = 0
        while pq:
            dis,node = heapq.heappop(pq)
            if dist[node]<dis:
                continue 
            for nei,wei in adj[node]:
                cost = dist[node]+wei
                if cost<dist[nei]:
                    dist[nei] = cost 
                    heapq.heappush(pq,(cost,nei))
        for i in range(1,n+1):
            if dist[i] == float('inf'):
                return -1 
        return max(dist[1:])
        