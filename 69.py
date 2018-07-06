class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low < high:
            mid = (low + high + 1) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                high = mid - 1
            else:
                low = mid
        return low