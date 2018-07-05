class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            res = res * 26 + ord(i) - 64
        return res