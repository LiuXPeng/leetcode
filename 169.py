class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = None
        count = 0
        for i in nums:
            if i == cur:
                count += 1
            else:
                if count == 0:
                    cur = i
                    count += 1
                else:
                    count -= 1
        return cur