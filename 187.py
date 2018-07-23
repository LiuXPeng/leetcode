class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strs = set()
        res = []
        for i in range(len(s) - 9):
            temp = 0
            for j in range(10):
                if s[i+j] == 'A':
                    temp = temp * 4
                if s[i+j] == 'C':
                    temp = temp * 4 + 1
                if s[i+j] == 'G':
                    temp = temp * 4 + 2
                if s[i+j] == 'T':
                    temp = temp * 4 + 3
            if temp in strs:
                if not s[i:i + 10] in res:
                    res.append(s[i:i + 10])
            else:
                strs.add(temp)
        return res