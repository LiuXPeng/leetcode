class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for s in strs:
            k = min(len(res), len(s))
            temp = 0
            for i in range(k):
                temp = i
                if s[i] != res[i]:
                    break
                else:
                    temp += 1
            if temp == 0:
                return ''
            res = res[:temp]
        return res