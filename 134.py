class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        label = 0
        for i in range(len(cost)):
            gas[i] -= cost[i]
            label += gas[i]
        if label < 0:
            return -1
        for i in range(len(cost)):
            temp = 0
            for j in (range(i, len(cost)) + range(0, i)):
                temp += gas[j]
                if temp < 0:
                    break
            if temp == label:
                return i