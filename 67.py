class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = n = 0
        for i in a:
            if i == '1':
                m = m * 2 + 1
            else:
                m = m * 2
        for i in b:
            if i == '1':
                n = n * 2 + 1
            else:
                n = n * 2
        m += n
        if m == 0:
            return '0'
        res = ''
        while m > 1:
            if m % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res
            m = m // 2
        if m == 1:
            res = '1' + res
        return res