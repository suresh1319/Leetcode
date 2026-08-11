class Solution {
    public void solve(char[][] board) {
        int n = board.length;
        int m = board[0].length;
        int[][] visited = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                visited[i][j] = 0;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if((i==0 || j == 0 || i == n-1 || j == m-1) && board[i][j] == 'O' && visited[i][j] == 0){
                    dfs(visited,board,i,j);
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(visited[i][j] == 0 && board[i][j]=='O'){
                    board[i][j] = 'X';
                }
            }
        }
    }
     static void dfs(int[][] visited,char[][] board,int row,int col){
            int n = visited.length;
            int m = visited[0].length;
            visited[row][col] = 1;
            int[][] direc = {{1,0},{-1,0},{0,-1},{0,1}};
            for(int i = 0;i<direc.length;i++){
                int nr = row+direc[i][0];
                int nc = col+direc[i][1];
                if(nr>=0 && nr<n && nc>=0 && nc<m && board[nr][nc] == 'O' && visited[nr][nc]==0){
                    dfs(visited,board,nr,nc);
                }
            }
        } 
}