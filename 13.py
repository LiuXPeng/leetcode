class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tag = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = temp = res = 0
        for i in s:
            num = tag.get(i)
            if num == pre:
                temp += tag.get(i)
            elif num < pre:
                res = temp + res
                pre = num
                temp = pre
            else:
                res = res - temp
                pre = num
                temp = pre
        res = res + temp
        return res    