class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        flag = True
        mini = s[0]
        maxi = s[0]
        for i in range(1,n):
            if s[i-1]>s[i]:
                flag = False
            mini = min(mini,s[i])
            maxi = max(maxi,s[i]) 
        if flag:
            return 0 
        if len(s)<=2:
            return -1 
        if s[0] == mini or s[n-1] == maxi:
            return 1 
        has_mini_in_prefix = mini in s[:-1]
        has_maxi_in_suffix = maxi in s[1:]
        if not has_mini_in_prefix and not has_maxi_in_suffix:
            return 3
        return 2
        