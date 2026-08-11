class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            temp = num 
            summ = 0
            while num!=0:
                rem = num%10 
                summ += rem 
                num = num//10 
            num = summ 
        return num