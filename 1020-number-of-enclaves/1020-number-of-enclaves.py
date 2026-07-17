class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if (i==m-1 or i == 0 or j == 0 or j == n-1) and grid[i][j] == 1:
                    dq.append((i,j))
                    grid[i][j] = 0
        while dq:
            row,col = dq.popleft()
            direc = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr,dc in direc:
                nr,nc = row+dr,col+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    grid[nr][nc] = 0
                    dq.append((nr,nc))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans+=1
        return ans

