class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = []
        value = 1
        ans.append(value)
        for i in range(1,rowIndex+1):
            value *= rowIndex-i+1
            value = value//i
            ans.append(value)
        return ans