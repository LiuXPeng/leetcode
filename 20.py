class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                L.append(i)
            else:
                if len(L) == 0:
                    return False
                temp = L.pop()
                if i == ')' and temp != '(':
                    return False
                if i == ']' and temp != '[':
                    return False
                if i == '}' and temp != '{':
                    return False
        if len(L) != 0:
            return False
        return True