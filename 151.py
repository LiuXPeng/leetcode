class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = []
        temp = ''
        s += ' '
        for i in s:
            if i == ' ':
                if temp != '':
                    L.append(temp)
                    temp = ''
                continue
            temp = temp + i
        if len(L) == 0:
            return ''
        res = L[-1]
        for i in range(len(L) - 2, -1, -1):
            res = res + ' ' + L[i]
        return res