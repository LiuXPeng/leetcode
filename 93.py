class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L = []
        for i in s:
            L.append(ord(i) - 48)
        length = len(s)
        res = []
        def method(M, N, n):
            if n == 0:
                temp = 0
                if len(M) > 1 and M[0] == 0:
                    return
                for i in M:
                    temp = temp * 10 + i
                if temp < 256:
                    temp_ = ''
                    for i in M:
                        temp_ = temp_ + str(i)
                    res.append(N + temp_)
                return
            if len(M) - 1 >= n:
                method(M[1:], N + str(M[0]) + '.', n - 1)
            if len(M) - 2 >= n and M[0] != 0:
                temp = ''
                for i in M[:2]:
                    temp = temp + str(i)
                method(M[2:], N + temp + '.', n - 1)
            if len(M) - 3 >= n and M[0] != 0:
                temp = 0
                for i in M[:3]:
                    temp = temp * 10 + i
                if temp > 256:
                    return
                temp = ''
                for i in M[:3]:
                    temp = temp + str(i)
                method(M[3:], N + temp + '.', n - 1)
            return
        method(L, '', 3)
        return res