class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pairs = {i:[] for i in range(n)}
        for side1, side2 in edges:
            pairs[side1].append(side2)
            pairs[side2].append(side1)
        
        checked = set()
        def dfs(node,parent):
            if node in checked:
                return False
            checked.add(node)
            for pair in pairs[node]:
                if pair == parent:
                    continue
                if not dfs(pair, node):
                    return False

            return True
        
        if not dfs(0,-1):
            return False
        return len(checked) == n
