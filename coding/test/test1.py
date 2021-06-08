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
        count = {i:0 for i in range(0, 24)}
        for start, end in airplanes:
            for j in range(start, end):
                count[j] += 1
        return max(count.values())

s = Solution()
print(s.countOfAirplanes([(1,10),(2,3),(5,8),(4,7)]))