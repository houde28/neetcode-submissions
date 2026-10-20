class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        left = 0

        for i in range(len(s)):
            letter = s[i]
            while letter in seen:
                seen.remove(s[left])
                left += 1
            seen.add(letter)
            cur = i - left+1
            if cur > res:
                res = cur
        
        return res
                