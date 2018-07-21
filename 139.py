class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        m = 0
        for word in wordDict:
            if len(word) > m:
                m = len(word)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            j = i - m
            if j < 0:
                j = 0
            while j < i:
                if not dp[j]:
                    j += 1
                    continue
                #print(s[j:i])
                if s[j:i] in wordDict:
                    dp[i] = True
                    break
                j += 1
        return dp[-1]