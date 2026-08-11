class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            s = str(i)
            flag = True 
            for j in s:
                ele = int(j)
                if ele == 0 or i%ele != 0:
                    flag = False 
                    break 
            if flag:
                ans.append(i)
        return ans