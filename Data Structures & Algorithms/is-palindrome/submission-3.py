class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s=s.lower()
        while left <right:
            while not s[left].isalnum() and left < right:
                left +=1
            
            while not s[right].isalnum() and right >left:
                right -= 1
            
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        
        return True
