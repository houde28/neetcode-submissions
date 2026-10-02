class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        strr = ""
    
        def helper(index):
            if index == len(s):
                res.append(cur.copy())
                return
            
            for i in range(index, len(s)):
                piece = s[index:i+1]
                if piece == piece[::-1]:
                    cur.append(piece)
                    helper(i + 1)
                    cur.pop()
        helper(0)

        return res