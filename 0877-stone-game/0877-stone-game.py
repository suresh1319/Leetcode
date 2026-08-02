class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        aliceTurn = True 
        aliceScore = 0
        bobScore = 0
        n = len(piles)
        st = 0
        end = n-1
        while st<end:
            if aliceTurn:
                if piles[st]>piles[end]:
                    aliceScore += piles[st]
                    st+=1
                else:
                    aliceScore += piles[end]
                    end-=1
            else:
                if piles[st]>piles[end]:
                    bobScore += piles[end]
                    end -= 1
                else:
                    bobScore += piles[st]
                    st+=1
        return aliceScore>bobScore