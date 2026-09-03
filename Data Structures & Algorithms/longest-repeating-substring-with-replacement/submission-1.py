class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hash_table = {}
        max_length=0
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]]= 1
            else:
                hash_table[s[i]]+=1
            len_window = i-left+1
            
            diff = len_window - max(hash_table.values())
            if diff > k:
                hash_table[s[left]]-=1
                left+=1
            
            len_window = i-left+1
            if max_length < len_window:
                max_length = len_window
                
        return max_length