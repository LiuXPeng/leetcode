class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        tags = ['+', '-', '*', '/']
        for s in tokens:
            if s in tags:
                temp = res.pop()
                if s == '+':
                    res[-1] += temp
                if s == '-':
                    res[-1] -= temp
                if s == '*':
                    res[-1] *= temp
                if s == '/':
                    if res[-1]*temp < 0 and res[-1] % temp != 0:
                        res[-1] = res[-1] // temp + 1
                    else:
                        res[-1] //= temp
            else:
                res.append(int(s))
        return res[0]