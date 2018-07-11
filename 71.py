class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        S = path.split('/')
        temp = []
        res = ''
        for s in S:
            if s == '..':
                if len(temp) != 0:
                    temp.pop()
            elif s == '' or s == '.':
                continue
            else:
                temp.append(s)
        for i in temp:
            res = res + '/' + i
        if len(res) == 0:
            return '/'
        return res  