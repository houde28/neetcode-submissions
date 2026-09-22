import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]
            
        heap = []
        for each in stones:
            heapq.heappush(heap, -each)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,-(x-y))
            
            
        if not heap:
            return 0
        return abs(heap[0])
                


        