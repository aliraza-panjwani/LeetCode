class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        n1 = d[s[0]]
        for i in range(1,len(s)):
            n = n1
            n1 = d[s[i]]
            if n1 > n:
                sum -= n
            else:
                sum += n
        return sum + n1