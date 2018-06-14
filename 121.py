class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_ = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if profit < (prices[i] - min_):
                profit = prices[i] - min_
            if min_ > prices[i]:
                min_ = prices[i]
        return profit
