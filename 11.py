class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] > height[j]:
                j -= 1
                if height[j] > height[j + 1]:
                    res = max(res, (j - i) * min(height[i], height[j]))
            else:
                i += 1
                if height[i] > height[i - 1]:
                    res = max(res, (j - i) * min(height[i], height[j]))
        return res