class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        label1 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        label2 = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
        label3 = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
        label4 = {1:'M', 2:'MM', 3:'MMM'}
        res = ''
        k = num % 10
        num = num // 10
        if k != 0:
            res = label1[k] + res
        if num == 0:
            return res
        k = num % 10
        num = num // 10
        if k != 0:
            res = label2[k] + res
        if num == 0:
            return res
        k = num % 10
        num = num // 10
        if k != 0:
            res = label3[k] + res
        if num == 0:
            return res
        k = num % 10
        num = num // 10
        if k != 0:
            res = label4[k] + res
        return res   


#######################################
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
        return result