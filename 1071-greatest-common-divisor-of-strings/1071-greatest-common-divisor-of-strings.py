class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        if str1+str2 != str2+str1:
            return ""
        while n2!=0:
            n1,n2 = n2,n1%n2
        return str2[:n1]
            
