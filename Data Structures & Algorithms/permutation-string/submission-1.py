class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for right in range(len(s1),len(s2)+1):
            current_string = s2[left:right]
            if sorted(current_string) == sorted(s1):
                return True
           
            left += 1
        return False