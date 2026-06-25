class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        for i in range(floor(l/2)):
            print("i:", i, "val:", s[i], "-i:", -i-1, "val:", s[-i-1])
            if s[i] != s[-i-1]:
                return False
        return True
        