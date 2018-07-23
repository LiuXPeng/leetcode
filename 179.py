class strNum(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=strNum)
        ans = ''.join(map(str,nums))
        return '0' if ans[0]=='0' else ans

############################################
class strNum(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=strNum)
        ans = ''.join(map(str,nums))
        return '0' if ans[0]=='0' else ans