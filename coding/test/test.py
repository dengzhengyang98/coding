from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = self.get_indegree(numCourses, prerequisites)
        start_node = [x for x in range(numCourses) if indegree[x] == 0]
        q = deque(start_node)
        courses = list(range(numCourses))
        while q:
            course = q.popleft()
            for prerequisite in prerequisites:
                if course == prerequisite[1]:
                    indegree[prerequisite[0]] -= 1
                    if indegree[prerequisite[0]] == 0:
                        q.append(prerequisite[0])
            courses.remove(course)
        if len(courses) == 0:
            return True
        else:
            return False

    def get_indegree(self, numCourses, prerequisites):
        indegree = {x:0 for x in range(numCourses)}
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
        return indegree