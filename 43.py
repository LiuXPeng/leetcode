class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for i in num1:
            m = ord(i) - 48
            temp = 0
            for j in num2:
                n = ord(j) - 48
                temp = temp * 10 + m*n
            res = res * 10 + temp
        return str(res)