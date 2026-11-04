class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preq[course].append(pre)
        seen = set()
        def helper(course):
            if course in seen:
                return False
            
            if preq[course] == []:
                return True
            seen.add(course)
            for crs in preq[course]:
                if not helper(crs):
                    return False

            seen.remove(course)
            preq[course] = []
            return True

        for course in range(numCourses):
            if not helper(course):
                return False
        return True
                