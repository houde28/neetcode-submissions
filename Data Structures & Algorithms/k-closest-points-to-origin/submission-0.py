import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        result=[]
        for i in range(len(points)):
            curx, cury= points[i]
            edistance = math.sqrt((0-curx)**2 + (0-cury)**2)
            heapq.heappush(heap,(edistance,curx,cury))

        for i in range(k):
            e,curx,cury= heapq.heappop(heap)
            result.append([curx,cury])

        return result
            