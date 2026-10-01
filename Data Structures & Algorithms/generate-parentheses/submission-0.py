class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openn = 0
        closedn = 0
        res = []
        def helper(cur, openn, closedn):
            if openn == closedn == n:
                res.append(cur)
                return
            if openn < n:
                cur += "("
                helper(cur,openn+1, closedn)
                cur = cur[:-1]
            
            if closedn < openn:
                cur += ")"
                helper(cur, openn, closedn + 1)
        helper("",0,0)
        return res
            
