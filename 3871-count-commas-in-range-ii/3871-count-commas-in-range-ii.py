class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        summ = 0
        
        # 1 comma range: 1,000 to 999,999
        if n < 1000000:
            return (n - 1000 + 1)
        summ += (999999 - 1000 + 1)
        
        # 2 commas range: 1,000,000 to 999,999,999
        if n < 1000000000:
            summ += 2 * (n - 1000000 + 1)
            return summ
        summ += 2 * (999999999 - 1000000 + 1)
        
        # 3 commas range: 1,000,000,000 to 999,999,999,999
        if n < 1000000000000:
            summ += 3 * (n - 1000000000 + 1)
            return summ
        summ += 3 * (999999999999 - 1000000000 + 1)
        
        # 4 commas range: 1,000,000,000,000 to 999,999,999,999,999
        if n < 1000000000000000:
            summ += 4 * (n - 1000000000000 + 1)
            return summ
        summ += 4 * (999999999999999 - 1000000000000 + 1)
        
        # 5 commas range: 1,000,000,000,000,000 to n
        summ += 5 * (n - 1000000000000000 + 1)
        
        return summ
