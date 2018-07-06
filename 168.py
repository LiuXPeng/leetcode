class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            k = n % 26
            n = n // 26
            if k == 0:
                k = 26
                n -= 1
            res = chr(k + 64) + res
        return res

###################
class Solution:
    # @param s, a string
    # @return an integer
    def convertToTitle(self, num):
        ans = ''
        while num:
            ans = chr(ord('A') + (num-1)%26 )+ans
            num = (num-1)/26
        return ans