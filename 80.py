class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        flag = None
        flag2 = True
        for i in nums:
            if flag != i:
                flag = i
                flag2 = True
                nums[count] = i
                count += 1
            elif flag == i:
                if flag2 == False:
                    pass
                else:
                    flag2 = False
                    nums[count] = i
                    count += 1
        return count