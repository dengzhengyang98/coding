# Lint-125. Backpack II



有 `n` 个物品和一个大小为 `m` 的背包. 给定数组 `A` 表示每个物品的大小和数组 `V` 表示每个物品的价值.

问最多能装入背包的总价值是多大?

`A[i], V[i], n, m` 均为整数你不能将物品进行切分你所挑选的要装入背包的物品的总大小不能超过 `m`每个物品只能取一次

m <= 1000*m*<=1000\len(A),len(V)<=100*l**e**n*(*A*),*l**e**n*(*V*)<=100

样例

**样例 1：**

输入：

```
m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
```

输出：

```
9
```

解释：

装入 A[1] 和 A[3] 可以得到最大价值, V[1] + V[3] = 9

**样例 2：**

输入：

```
m = 10
A = [2, 3, 8]
V = [2, 5, 8]
```

输出：

```
10
```



```python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        # write your code here
        n = len(A)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # i为货物数量，j为重量
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+V[i-1])
        return dp[n][m]

```



```python
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackII(self, m, A, V):
        # write your code here
        f = [0 for i in range(m+1)]
        n = len(A)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                f[j] = max(f[j] , f[j-A[i]] + V[i])
        return f[m]
```

