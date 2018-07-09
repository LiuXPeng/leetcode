class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        tag = False
        temp = True
        res = 0
        for i in str:
            if i == '-' or i == '+':
                if temp:
                    if i == '-':
                        tag = True
                    temp = False
                    continue
                break
            if 48 <= ord(i) < 58:
                res = res * 10 + ord(i) - 48
                temp = False
                continue
            if i == ' ':
                if temp:
                    continue
                break
            break
        if tag:
            res = -res
        return min(max(-2147483648, res), 2147483647)