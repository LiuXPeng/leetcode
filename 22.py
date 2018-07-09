class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def method(value, m, k, L):
            if k == 0:
                res.append(L)
                return
            if m > 0:
                method(value + 1, m - 1, k, L + '(')
            if value > 0:
                method(value - 1, m, k - 1, L + ')')
            return
        res = []
        method(0, n, n, '')
        return res