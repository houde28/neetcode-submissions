class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preq[course].append(pre)
        seen, cycle = set(), set()
        res = []
        def helper(course):
            if course in cycle:
                return False
            if course in seen:
                return True         
            
            cycle.add(course)
            for crs in preq[course]:
                if helper(crs) == False:
                    return False

            cycle.remove(course)
            seen.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if helper(course) == False:
                return []
        return res