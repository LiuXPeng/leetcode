class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPali(s):
            j = len(s) - 1
            i = 0
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n = len(s)
        if n == 0:
            return [[]]
        res = []
        for i in range(n):
            if isPali(s[:i+1]):
                for temp in self.partition(s[i + 1:]):
                    res.append([s[:i + 1]] + temp)
        return res