class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(row,col):
            visited[row][col] = 1
            direc = [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in direc:
                nr,nc = row+dr,col+dc
                if 0<=nr<n and 0<=nc<m and board[nr][nc] == 'O' and visited[nr][nc] == 0:
                    dfs(nr,nc)
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and board[i][j] == 'O' and visited[i][j] == 0:
                    dfs(i,j)

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"
        return board 