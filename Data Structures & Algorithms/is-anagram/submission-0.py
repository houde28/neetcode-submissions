class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictionary1 = {}
        dictionary2 = {}
        for each in s:
            if each in dictionary1:
                dictionary1[each]+=1
            else:
                dictionary1[each]=1
        for each in t:
            if each in dictionary2:
                dictionary2[each]+=1
            else:
                dictionary2[each]=1
        
        if dictionary1 == dictionary2:
            return True

        return False
        
        

