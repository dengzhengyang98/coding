# Union Find

```python
class UnionFind:
    def __init__(self):
        self.root = list(range(row*col))
       
    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            #这里是并查集优化，能够让所有节点直接指向父节点，从而find能直接找到父节点节省时间和防止递归的栈太多
            root[x] = self.find(self.root[x])
            return root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = rootY
```



