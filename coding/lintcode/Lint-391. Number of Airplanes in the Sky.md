# 391 · 数飞机

## 扫描线算法

https://marian5211.github.io/2017/11/17/%E3%80%90%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95%E5%BC%BA%E5%8C%96%E7%8F%AD%E3%80%91%E6%89%AB%E6%8F%8F%E7%BA%BF/

给出飞机的起飞和降落时间的列表，用序列 `interval` 表示. 请计算出天上同时最多有多少架飞机？

如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

**样例 1:**

```
输入: [(1, 10), (2, 3), (5, 8), (4, 7)]
输出: 3
解释: 
第一架飞机在1时刻起飞, 10时刻降落.
第二架飞机在2时刻起飞, 3时刻降落.
第三架飞机在5时刻起飞, 8时刻降落.
第四架飞机在4时刻起飞, 7时刻降落.
在5时刻到6时刻之间, 天空中有三架飞机.
```

**样例 2:**

```
输入: [(1, 2), (2, 3), (3, 4)]
输出: 1
解释: 降落优先于起飞.
```



- 记录起飞和降落的时间点，然后按时间进行排序，用delta作为动态的存储，飞的加1，降落的减1
- ```sorted(list(list))```返回按照list里的第一个元素的大小进行的排序

```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        points = []
        for airplane in airplanes:
            points.append([airplane.start, 1])
            points.append([airplane.end, -1])
        result, delta = 0, 0
        for point in sorted(points):
            delta += point[1]
            result = max(result, delta)
        return result
```

