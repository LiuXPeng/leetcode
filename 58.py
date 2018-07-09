class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        temp = 0
        for i in s:
            if i == ' ':
                if res != 0:
                    temp = res
                res = 0
            else:
                res += 1
        if res == 0:
            res = temp
        return res