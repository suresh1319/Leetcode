import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        dist = [[float('inf')]*m for _ in range(n)]
        pq = []
        dist[0][0] = 0
        heapq.heappush(pq,(0,0,0))
        direc = [[-1,0],[1,0],[0,1],[0,-1]]
        while pq:
            eff,r,c = heapq.heappop(pq)
            if r==n-1 and c == m-1:
                return eff
            for dr,dc in direc:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m:
                    currEff = max(eff,abs(heights[nr][nc]-heights[r][c]))
                    if currEff<dist[nr][nc]:
                        dist[nr][nc] = currEff
                        heapq.heappush(pq,(currEff,nr,nc))
        return 0