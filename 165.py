class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        i = 0
        while i < len(v1) and i < len(v2):
            if v1[i] != v2[i]:
                temp1 = 0
                temp2 = 0
                for j in v1[i]:
                    temp1 = temp1 * 10 + ord(j) - 48
                for j in v2[i]:
                    temp2 = temp2 * 10 + ord(j) - 48
                if temp1 > temp2:
                    return 1
                if temp1 < temp2:
                    return -1
            i += 1
        if len(v1) > len(v2):
            while i < len(v1):
                for j in v1[i]:
                    if j != '0':
                        return 1
                i += 1
        if len(v2) > len(v1):
            while i < len(v2):
                for j in v2[i]:
                    if j != '0':
                        return -1
                i += 1
        return 0