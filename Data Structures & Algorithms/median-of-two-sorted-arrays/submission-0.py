class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        half = (len(nums1) + len(nums2)+1) // 2
        left = 0
        right = len(nums1)
        total = len(nums1) + len(nums2)

        while left <= right:
            split1 = (left+right) // 2
            split2 = half - split1
            nums1_left = nums1[split1-1] if split1 > 0 else float("-inf")
            nums1_right = nums1[split1] if split1 < len(nums1) else float("inf")
            nums2_left = nums2[split2-1] if split2 > 0 else float("-inf")
            nums2_right = nums2[split2] if split2 < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left,nums2_left) + min(nums1_right,nums2_right)) / 2
            else:
                if nums1_left >nums2_right:
                    right = split1 - 1
                else:
                    left = split1 + 1
                
        return 0


        
            
             

            