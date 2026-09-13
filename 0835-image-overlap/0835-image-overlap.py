class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1Ones = []
        img2Ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1Ones.append((i,j))
                if img2[i][j] == 1:
                    img2Ones.append((i,j))
        freq = {}
        for x1,y1 in img1Ones:
            for x2,y2 in img2Ones:
                x,y = x2-x1,y2-y1
                freq[(x,y)] = freq.get((x,y),0)+1
        if not freq:
            return 0 
        return max(freq.values())
        
        