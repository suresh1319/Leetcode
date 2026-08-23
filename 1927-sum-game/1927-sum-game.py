class Solution:
    def sumGame(self, num: str) -> bool:
        leftSum = 0
        rightSum = 0
        leftQues = 0
        rightQues = 0 
        n = len(num)
        for i in range(n):
            if i<n//2:
                if num[i] == '?':
                    leftQues += 1
                else:
                    leftSum += int(num[i])
            else:
                if num[i] == '?':
                    rightQues += 1 
                else:
                    rightSum += int(num[i])
        if (leftQues+rightQues)%2 == 1:
            return True 
        return 2*(leftSum-rightSum) != (rightQues-leftQues)*9
        