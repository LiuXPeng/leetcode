class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for i in strs:
            l = sorted(i)
            key = "".join(l)
            if key in res.keys():
                res[key] = res[key] + [i]
            else:
                res[key] = [i]
        return list(res.values())