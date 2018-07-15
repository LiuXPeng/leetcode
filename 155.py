class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []
        self.minStack = []
        self.length = 0
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.L.append(x)
        self.length += 1
        i = 0
        while i < self.length - 1:
            if x > self.minStack[i]:
                break
            i += 1
        self.minStack.insert(i, x)
        return
        
        
    def pop(self):
        """
        :rtype: void
        """
        if self.length == 0:
            return
        self.length -= 1
        temp = self.L.pop()
        self.minStack.remove(temp)
        return
        

    def top(self):
        """
        :rtype: int
        """
        if self.length > 0:
            return self.L[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.length > 0:
            return self.minStack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()