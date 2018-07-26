class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        temp = []
        while n > 1:
            if n % 2:
                temp.append(1)
            else:
                temp.append(0)
            print(n, temp[-1])
            n = n // 2
        temp.append(1)
        for i in range(len(temp), 32):
            temp.append(0)
        res = 0
        for i in temp:
            res = res * 2 + i
        return res