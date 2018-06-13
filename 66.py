class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in digits:
            sum = sum * 10 + i
        sum = sum + 1
        L = []
        while sum != 0:
            L.insert(0, sum % 10)
            sum = sum // 10
        return L