class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = [[], [nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                for L in res:
                    try:
                        if L[-1] == nums[i]:
                            res.append(L + [nums[i]])
                    except:
                        continue     
            else:
                for L in res:
                    res.append(L + [nums[i]])
        return res