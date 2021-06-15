# Lint-92. Backpack



在`n`个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为`m`，每个物品的大小为A_{i}*A**i*

你不可以将物品进行切割。

样例

**样例 1：**

输入：

```
数组 = [3,4,8,5]
backpack size = 10
```

输出：

```
9
```

解释：

装4和5.

**样例 2：**

输入：

```
数组 = [2,3,5,7]
backpack size = 12
```

输出：

```
12
```

解释：

装5和7.



## dp

如果第n个物品```A[i-1]```大于当前重量`j`，则等于上一个重量的相同重量`dp[i][j]=dp[i-1][j]` ，否则就取上一个重量和`dp[i-1][j-A[i-1]]+A[i-1]`（查表[上一个货物数量，当前重量-新货物重量]+新货物重量）的较大值

这里之所以要n+1是因为n为货物数量，会访问到n，m+1是因为同样会访问到m重量

```python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # i为货物数量，j为重量
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+A[i-1])
        return dp[n][m]
```



- 倒序枚举j是防止较大的因为前面的值已经存在而导致混乱

```python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # 如果背包容量或者物品数量为0，则直接返回
        if m == 0 or len(A) == 0:
            return 0

        dp = [0 for _ in range(m + 1)]
        for i in range(len(A)):
            # 滚动数组优化 倒序枚举j
            for j in range(m, A[i] - 1, -1):
                # A[i] - 1是作为筛选条件，i<A[i]的就不用遍历了
                dp[j] = max(dp[j], dp[j - A[i]] + A[i])

        return dp[m]
s = Solution()
print(s.backPack(10 ,[3,4,8,5]))
```

