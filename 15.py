class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        first = 0
        second = 1
        third = len(nums) - 1
        while second < third:
            if nums[first] + nums[second] + nums[third] == 0:
                res.append([nums[first], nums[second], nums[third]])
                temp = nums[second]
                while second < third:
                    if temp == nums[second]:
                        second += 1
                    else:
                        break
            elif nums[first] + nums[second] + nums[third] < 0:
                second += 1
            else:
                third -= 1
        for first in range(1, len(nums) - 2):
            if nums[first] > 0:
                break
            if nums[first] == nums[first - 1]:
                continue
            else:
                second = first + 1
                third = len(nums) - 1
                while second < third:
                    if nums[third] < 0:
                        break
                    if nums[first] + nums[second] + nums[third] == 0:
                        res.append([nums[first], nums[second], nums[third]])
                        third -= 1
                        while second < third:
                            if nums[third + 1] == nums[third]:
                                third -= 1
                            else:
                                break
                    elif nums[first] + nums[second] + nums[third] < 0:
                        second += 1
                    else:
                        third -= 1
        return res