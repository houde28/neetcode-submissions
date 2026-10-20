class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for each in strs:
            counts = [0]*26

            for letter in each:
                index = ord(letter) - ord('a')
                counts[index] += 1
            
            freq = tuple(counts)

            if freq not in res:
                res[freq] = []
            
            res[freq].append(each)
        
        return list(res.values())
        
        
            

