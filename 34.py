class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = [0, 0]
                if right - left <= 8:
                    for x in range(left, mid + 1):
                        if target == nums[x]:
                            res[0] = x
                            break
                    for y in range(right, mid - 1, -1):
                        if target == nums[y]:
                            res[1] = y
                            break
                    return res
                temp = mid
                i = left
                j = temp
                while i < j:
                    mid = (i + j) // 2
                    if nums[mid] == target:
                        j = mid
                    else:
                        i = mid + 1
                res[0] = i
                i = temp
                j = right
                while i < j:
                    mid = (i + j + 1) // 2
                    if nums[mid] == target:
                        i = mid
                    else:
                        j = mid - 1
                    print(i, mid, j)
                res[1] = i
                return res
        return [-1, -1]




#提高里面最快的代码
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.firstGreaterEqaul(nums, target)
        if start==len(nums) or nums[start]!=target:
            return [-1, -1]
        return [start, self.firstGreaterEqaul(nums, target+1)-1]
    def firstGreaterEqaul(self, nums, target):
        lo, hi = 0, len(nums)
        while lo<hi:
            mid = (hi+lo)//2
            if nums[mid]<target:
                lo = mid + 1
            else:
                hi = mid
        return lo