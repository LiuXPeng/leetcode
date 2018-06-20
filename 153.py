class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] > nums[-1]:
            low = len(nums) - 1
            high = 0
        else:
            return nums[0]
        while low != high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                high = mid
            elif nums[mid] < nums[low]:
                low = mid
            else:
                break
            if nums[high] < nums[low]:
                temp = high
                high = low
                low = temp
        return nums[low]

#####better method
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] > nums[-1]:
            low = len(nums) - 1
            high = 0
        else:
            return nums[0]
        while abs(low - high) > 1:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                high = mid
            else:
                low = mid            
        return nums[low]