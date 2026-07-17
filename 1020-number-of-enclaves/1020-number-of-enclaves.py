class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if (i==m-1 or i == 0 or j == 0 or j == n-1) and grid[i][j] == 1:
                    dq.append((i,j))
                    visited[i][j] = 1
        while dq:
            row,col = dq.popleft()
            direc = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr,dc in direc:
                nr,nc = row+dr,col+dc
                if 0<=nr<m and 0<=nc<n and visited[nr][nc]==0 and grid[nr][nc]==1:
                    visited[nr][nc] = 1
                    dq.append((nr,nc))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==0:
                    ans+=1
        return ans

