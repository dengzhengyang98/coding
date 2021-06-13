# Lint-127. Topological Sorting



1. get_indegree
2. 选择indegree为0的node为```start_node```
3. bfs

```python
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_to_indegree = self.get_indegree(graph)
        
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        q = collections.deque(start_nodes)

        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)
        return order

    
    def get_indegree(self, graph):
        node_to_indegree = {x:0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        return node_to_indegree
```

