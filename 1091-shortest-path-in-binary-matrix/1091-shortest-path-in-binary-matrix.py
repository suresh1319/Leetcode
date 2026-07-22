import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        pq = []
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 1

        heapq.heappush(pq, (1, 0, 0))

        direc = [
            [-1,0],[1,0],[0,-1],[0,1],
            [1,1],[-1,-1],[-1,1],[1,-1]
        ]

        while pq:
            wei, r, c = heapq.heappop(pq)

            if r == n - 1 and c == m - 1:
                return wei

            if wei > dist[r][c]:
                continue

            for dr, dc in direc:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    dis = wei + 1

                    if dis < dist[nr][nc]:
                        dist[nr][nc] = dis
                        heapq.heappush(pq, (dis, nr, nc))

        return -1