# BFS

- 一般和Queue搭配使用
- 逐层向下搜索



## lc938

<img src="C:\Users\Zhengyang\AppData\Roaming\Typora\typora-user-images\image-20210529161610591.png" alt="image-20210529161610591" style="zoom:50%;" />



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = deque()
        q.append(root)
        result = self.bfs(q, low, high)
        return result
        
    def bfs(self, q, low, high):
        result = 0
        while len(q) > 0:
            node = q.popleft()
            if node.val >= low and node.val <= high:
                result += node.val
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return result    
            
```

