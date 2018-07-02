class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxP = nums[0]
        minP = nums[0]
        i = 1
        res = nums[0]
        while i < len(nums):
            temp = maxP
            maxP = max(nums[i], nums[i] * temp, nums[i] * minP)
            minP = min(nums[i], nums[i] * temp, nums[i] * minP)
            i += 1
            res = max(maxP, res)
        return res

        
##############
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = -float("inf")
        product = 1
        for num in nums:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        product = 1
        for num in nums[::-1]:
            product *= num
            max_val = max(product, max_val)
            if num == 0:
                product = 1
        return max_val