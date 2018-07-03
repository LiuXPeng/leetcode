class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        k = len(nums)
        nums.sort()
        if k < 4 or nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        sol = []
        for i in range(k - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target1 = target - nums[i]
            for j in range(i + 1, k - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target2 = target1 - nums[j]
                m = j + 1
                n = k - 1
                while m < n:
                    res = nums[m] + nums[n]
                    if res == target2:
                        sol.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                        while m < n and nums[n] == nums[n + 1]:
                            n -= 1
                    elif res > target2:
                        n -= 1
                    else:
                        m += 1
        return sol