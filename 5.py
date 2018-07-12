class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'
        for i in s:
            T = T + i + '#'
        centor = 0
        right = 0
        P = [0] * len(T)
        for i in range(len(T)):
            mirror = 2 * centor - i
            if i < right - P[mirror]:
                P[i] = P[mirror]
            elif i < right and i + P[mirror] >= right:
                P[i] = right - i#这里不是P[i] = P[mirror]
                j = right - i + 1
                while i - j >= 0 and j + i < len(T):
                    if T[i - j] == T[i + j]:
                        P[i] = P[i] + 1
                        j += 1
                    else:
                        break
            else:
                j = 1
                while i - j >= 0 and j + i < len(T):
                    if T[i - j] == T[i + j]:
                        P[i] = P[i] + 1
                        j += 1
                    else:
                        break
            if P[i] + i > right:
                centor = i
                right = P[i] + i
        temp = 0
        j = 0
        for i in range(len(P)):
            if P[i] > temp:
                temp = P[i]
                j = i
        res1 = T[j]
        for i in range(temp):
            res1 = T[j - 1 - i] + res1+ T[j + 1 + i]
        res = ''
        for i in res1:
            if i != '#':
                res = res + i
        return res