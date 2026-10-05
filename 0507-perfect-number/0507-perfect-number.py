class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1
        i = 2
        if num <= 1:
            return False
        while i*i <= num:
            if num%i == 0:
                total += i
                if i*i != num:
                    total += num//i
            i+=1
        return total == num