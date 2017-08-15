class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

a=Solution()
b=a.romanToInt('XVI')
print(b)
