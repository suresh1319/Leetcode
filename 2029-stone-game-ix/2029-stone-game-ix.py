class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        rem = [0]*3
        n = len(stones)
        for i in range(n):
            rem[stones[i]%3] += 1
        if rem[0]%2 == 0:
            return rem[1]>=1 and rem[2]>=1
        else:
            return abs(rem[1]-rem[2])>2
        
        