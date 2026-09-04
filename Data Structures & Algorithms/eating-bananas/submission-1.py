import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left= 1
        right = max(piles)
        min_k = right
        while left <= right:
            k = (left+right)//2
            hours=0
            for val in piles:
                hours += math.ceil(val/k)
            if hours <= h and k < min_k:
                min_k = k
                right = k -1
            else:
                left = k+1
        return min_k




