class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pairs = {i:[] for i in range(1, len(edges)+1)}
        seen = set()
        def dfs(n1,target):
            if n1 == target:
                return True
            
            seen.add(n1)

            for neighbor in pairs[n1]:
                if neighbor not in seen:
                    if dfs(neighbor, target):
                        return True
            return False
        
        for edge1, edge2 in edges:
            seen = set()
            if dfs(edge1,edge2):
                return [edge1,edge2]
            else:
                pairs[edge1].append(edge2)
                pairs[edge2].append(edge1)
