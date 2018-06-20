class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def method(index, sums, L):
            if index >= len(candidates):
                return
            while sums < target:
                method(index + 1, sums, L + [])
                sums = sums + candidates[index]               
                L.append(candidates[index])
                if sums == target:
                    res.append(L)
                    return
            return
        method(0, 0, [])
        return res 