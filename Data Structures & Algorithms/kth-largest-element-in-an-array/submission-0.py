import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for each in nums:
            heapq.heappush(heap,-each)

        counter = 0
        while counter < k-1:
            heapq.heappop(heap)
            counter +=1
        
        return -heap[0]