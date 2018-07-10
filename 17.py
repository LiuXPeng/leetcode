class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], \
              '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        res = ['']
        for i in digits:
            L = dic[i]
            temp = copy.deepcopy(res)
            res = []
            for l in L:
                for s in temp:
                    res.append(s + l)
        return res