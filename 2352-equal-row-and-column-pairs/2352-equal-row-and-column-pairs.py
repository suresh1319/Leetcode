class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}
        n = len(grid)
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[i][j])
            freq[tuple(temp)] = freq.get(tuple(temp),0)+1
        colFreq = {}
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            colFreq[tuple(temp)] = colFreq.get(tuple(temp),0)+1
        totalPairs = 0
        for key,val in freq.items():
            if key in colFreq:
                totalPairs += val * colFreq[key]
        return totalPairs