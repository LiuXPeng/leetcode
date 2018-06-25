class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def method(cur_sum, index, temp):
            temp = temp + [candidates[index]]
            cur_sum = cur_sum + candidates[index]
            if cur_sum == target:
                res.append(temp)
                return
            if cur_sum > target:
                return
            for i in range(index + 1, len(candidates)):
                if candidates[i] == candidates[i - 1] and i > index + 1:
                    continue
                method(cur_sum, i, temp)
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            method(0, i, [])
        return res

##########
class Solution:
    def combinationSum2(self, candidates, target):
                
        def dfs(i, val, path):
            while i < len(candidates):
                num = candidates[i]
                val_ = val + num
                path_ = path + [num]
                if val_ > target:
                    return
                elif val_ == target:
                    ans.append(path_)
                    return                  
                dfs(i+1, val_, path_)
                while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                    i += 1
                i += 1
               
        candidates = sorted(candidates)
        ans = []
        dfs(0, 0, [])
        return ans