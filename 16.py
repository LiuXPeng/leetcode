class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return
        nums.sort()
        second = 1
        third = len(nums) - 1
        res = nums[0] + nums[2] + nums[1]
        while second < third:
            temp = nums[0] + nums[second] + nums[third]
            if temp == target:
                return temp
            elif temp < target:
                second += 1
            else:
                third -= 1
            if abs(temp - target) < abs(res - target):
                res = temp
        for first in range(1, len(nums) - 2):
            if nums[first] == nums[first - 1]:
                continue
            else:
                second = first + 1
                third = len(nums) - 1
                while second < third:
                    temp = nums[first] + nums[second] + nums[third]
                    if temp == target:
                        return temp
                    elif temp < target:
                        second += 1
                    else:
                        third -= 1
                    if abs(temp - target) < abs(res - target):
                        res = temp
        return res