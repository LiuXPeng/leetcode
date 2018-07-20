class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0
        for i in nums:
            one = one ^ i
            two = (~one & i) ^ two
            three = one & two
            one = (~ three) & one
            two = ~ three & two
        return one