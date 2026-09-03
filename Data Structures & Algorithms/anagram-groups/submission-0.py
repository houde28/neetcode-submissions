class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result ={}
        for word in strs:
            count = [0]*26

            for character in word:
                index =ord(character) -ord('a')
                count[index] += 1
            
            key = tuple(count)

            if key not in result:
                result[key] = []    

            result[key].append(word)
        return list(result.values()) 