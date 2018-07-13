class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        DP = [0] * len(s)
        if s[0] == '0':
            return 0
        DP [0] = 1
        if len(s) == 1:
            return 1
        if s[1] != '0':
            DP[1] += 1
        if s[0] == '1':
            DP[1] += 1
        if s[0] == '2' and (s[1] == '0' or s[1] == '1' or s[1] == '2' or s[1] == '3' or s[1] == '4' or s[1] == '5' or s[1] == '6'):
            DP[1] += 1
        i = 2
        while i < len(s):
            if s[i] != '0':
                DP[i] = DP[i - 1]
            if s[i - 1] == '1':
                DP[i] += DP[i - 2]
            if s[i - 1] == '2' and (s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6'):
                DP[i] += DP[i - 2]
            i += 1
        print(DP)
        return DP[-1]