class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for _ in nums:
            temp = copy.deepcopy(res)
            for L in temp:
                L.append(_)
            res = res + temp
        return res