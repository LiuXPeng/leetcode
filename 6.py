class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        temp = []
        for i in range(numRows):
            temp.append([])
        i = 0
        while i < length:
            for L in temp:
                if i >= length:
                    break
                L.append(s[i])
                i += 1
            for j in range(numRows - 2, 0, -1):
                if i >= length:
                    break
                temp[j].append(s[i])
                i += 1
        res = ''
        for L in temp:
            for l in L:
                res = res + l
        return res