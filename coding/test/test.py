from typing import List
from operator import itemgetter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted(intervals, key=itemgetter(0))
        result = [intervals[0]]
        curr_idx = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            curr_start, curr_end = result[curr_idx][0], result[curr_idx][1]
            if start <= curr_end:
                if end > curr_end:
                    result[curr_idx] = [curr_start, end]
                else:
                    result[curr_idx] = [curr_start, curr_end]
            else:
                result.append([start, end])
                curr_idx += 1
        return result

s = Solution()
print(s.merge([[1,4],[0,4]]))