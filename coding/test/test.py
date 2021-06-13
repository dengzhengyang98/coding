from typing import List
import collections
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q = collections.deque()
        q.append([start[0], start[1]])
        row, col = len(maze), len(maze[0])
        visited = [[float('inf') for _ in range(row)] for _ in range(col)]
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        paths = []
        visited[start[0]][start[1]] = 0
        while q:
            p = q.popleft()
            for d1, d2 in directions:
                x ,y = p
                count = 0
                while x+d1 < row and x+d1 >= 0 and y+d2 < col and y+d2 >= 0 and maze[x+d1][y+d2] != 1:
                    x += d1
                    y += d2
                    count += 1
                if visited[p[0]][p[1]]+count < visited[x][y]:
                    visited[x][y] = visited[p[0]][p[1]] + count
                    q.append([x, y])
        print(visited)
        return -1 if visited[destination[0]][destination[1]] == float('inf') else visited[destination[0]][destination[1]]

s = Solution()
print(s.shortestDistance([[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]], [0,0], [8,6]))