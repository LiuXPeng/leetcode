class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)
        res = ''
        if numerator / denominator < 0:
            res += '-'
        label = []
        label2 = []
        numerator = abs(numerator)
        denominator = abs(denominator)
        temp = numerator // denominator
        numerator = numerator % denominator
        res += str(temp)
        res += '.'
        temp = len(res)
        while numerator != 0:
            if numerator in label:
                k = label.index(numerator)
                res=res[:k + temp]+"("+res[k + temp:]+")"
                return res
            label.append(numerator)
            numerator = numerator * 10
            res += str(numerator // denominator)
            numerator = numerator % denominator 
        return res