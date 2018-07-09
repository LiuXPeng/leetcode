class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1
        res = '1'
        for _ in range(n):
            temp = ''
            tag = res[0]
            count = 0
            for i in res:
                if i == tag:
                    count += 1
                else:
                    temp = temp + str(count) + tag
                    count = 1
                    tag = i
            res = temp + str(count) + tag
        return res