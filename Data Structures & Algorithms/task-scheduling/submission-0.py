import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        counter={}
        for each in tasks:
            if each in counter:
                counter[each] -= 1
            else:
                counter[each] = -1
        
        for each in counter:
            heapq.heappush(heap,(counter[each],each))

        timer=0
        while heap or queue:
            timer += 1
            while queue and queue[0][1] == timer:
                letter, time, count = queue.popleft()
                heapq.heappush(heap,(count,letter))

            if heap:
                val, letter= heapq.heappop(heap)
                val += 1
                if val < 0:
                    queue.append((letter,timer + n + 1,val))
            
        return timer 