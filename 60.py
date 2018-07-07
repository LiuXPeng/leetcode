class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k - 1
        m = 1
        tag = []
        res = ''
        for i in range(1, n + 1):
            m *= i
            tag.append(i)
        for i in range(n, 0, -1):
            m = m // i
            j = k // m
            k = k % m
            res = res + str(tag[j])
            del tag[j]
            if k == 0:
                for j in tag:
                    res = res + str(j)
                return res