class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = 0
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        while x > y:
            y = y * 10 + x % 10
            if y == x:
                return True
            x = x // 10
            if y == x:
                return True
        return False