from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        odq = deque()
        visited = [[0]*n for _ in range(n)]
        direc = [[-1,0],[1,0],[0,1],[0,-1]]
        def bfs(row,col):
            dq = deque()
            dq.append((row,col))
            odq.append((row,col))
            visited[row][col] = 1
            while dq:
                r,c = dq.popleft()
                for dr,dc in direc:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        odq.append((nr,nc))
                        dq.append((nr,nc))
        for i in range(n):
            flag = False 
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    bfs(i,j)
                    flag = True 
                    break 
            if flag == True:
                break
        self.ans = 0 
        def calculate():
            while odq:
                m = len(odq)
                for _ in range(m):
                    r,c = odq.popleft()
                    for dr,dc in direc:
                        nr,nc = r+dr,c+dc
                        if 0<=nr<n and 0<=nc<n and visited[nr][nc] == 0:
                            if grid[nr][nc] == 1:
                                return self.ans
                            else:
                                odq.append((nr,nc))
                                visited[nr][nc] = 1
                self.ans += 1
        return calculate() 

            
