class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ls = []
        for i in range(m):
            for j in range(n):
                ls.append(grid[i][j])
        def reverse(st,end,ls):
            l = st
            e = end
            while l<e:
                ls[l],ls[e] = ls[e],ls[l]
                l+=1
                e-=1
        size = len(ls)
        k = k%size
        reverse(0,size-1,ls)
        reverse(0,k-1,ls)
        reverse(k,size-1,ls)
        k=0
        for i in range(m):
            for j in range(n):
                grid[i][j] = ls[k]
                k+=1
        return grid