class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        vals = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []
        if digits == "":
            return res

        def helper(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for c in vals[digits[i]]:
                helper(i+1, cur+ c)

        helper(0,"")
        return res
