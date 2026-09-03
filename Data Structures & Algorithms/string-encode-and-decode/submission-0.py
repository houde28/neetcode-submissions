class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for each in strs:
            string+= str(len(each))+"_"+each 
        return string
    def decode(self, s: str) -> List[str]:
        result =[]
        index=0
        while index < len(s):
            length = 0
            while s[index] != "_":
                length = 10 * length + int(s[index])
                index+=1
            index += 1

            word = s[index:index+length]
            result.append(word)
            index += length
        return result

