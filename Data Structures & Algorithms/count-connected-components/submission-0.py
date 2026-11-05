class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pairs = {i:[] for i in range(n)}
        for side1, side2 in edges:
            pairs[side1].append(side2)
            pairs[side2].append(side1)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return 0
            seen.add(node)
            for edge in pairs[node]:
                if edge == parent:
                    continue
                dfs(edge, node)
            return 1
        
        res = 0
        for pair in pairs:
            if pair in seen:
                continue
            dfs(pair,-1)
            res += 1
        
        return res
            
            
