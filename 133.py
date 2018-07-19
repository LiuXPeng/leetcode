# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    global visited
    visited = {}
    def cloneGraph(self, node):
        global visited
        if node == None:
            return
        res = UndirectedGraphNode(node.label)
        visited[node] = res
        for i in node.neighbors:
            if i in visited:
                res.neighbors.append(visited.get(i))
            else:
                visited[i] = self.cloneGraph(i)
                res.neighbors.append(visited.get(i))
        return res