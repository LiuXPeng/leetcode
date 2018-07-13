class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tag = {}
        res = 0
        temp = 0
        for i in range(len(s)):
            if s[i] in tag:
                pre = tag.get(s[i])
                temp = min(temp + 1, i - pre)
            else:
                temp = temp + 1
            if temp > res:
                res = temp
            tag[s[i]] = i
        return res