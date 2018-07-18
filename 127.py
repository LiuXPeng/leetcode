class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not (endWord in wordList):
            return 0
        wordList = set(wordList)
        visited = set([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)
        dist = 1
        while visited:
            dist += 1
            temp = []
            for word in visited:
                for i in range(len(word)):
                    chars = list(word)
                    for j in range(ord('a'), ord('z') + 1):
                        chars[i] = chr(j)
                        newWord = ''.join(chars)
                        if newWord == endWord:
                            return dist
                        if newWord in wordList:
                            wordList.remove(newWord)
                            temp.append(newWord)
            if not temp:
                return 0
            visited = set(temp)
        return dist