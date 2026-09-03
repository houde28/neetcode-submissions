class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        char_t= {}
        window = {}
        for character in t:
            if character not in char_t:
                char_t[character] = 1
            else:
                char_t[character] += 1
        left = 0
        right = 0
        need=len(char_t)
        smallest = 100000
        small_left =0
        small_right= 0
        have= 0

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1


            if s[right] in char_t and window[s[right]] == char_t[s[right]]:
                have+=1

            while have == need:
                if right-left +1 < smallest:
                    smallest  = right-left+1
                    small_left= left
                    small_right = right

                if s[left] in char_t and window[s[left]] == char_t[s[left]]:
                    have -= 1

                window[s[left]] -= 1
                left += 1
                
            
            right+=1
        

        if smallest == 100000:
            return ""
        return s[small_left:small_right+1]
            

            

            
            


            
        

    