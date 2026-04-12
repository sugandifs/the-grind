class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0

        nodeMap = {node:[] for node in range(n)}

        for l, r in edges:
            nodeMap[l].append(r)
            nodeMap[r].append(l)

        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return 0
            
            visited.add(node)

            for neighbor in nodeMap[node]:
                if neighbor == parent:
                    continue

                dfs(neighbor, node)
            
            return 1
        

        for i in range(n):
            if i in visited:
                continue
            
            count += dfs(i, -1)
        
        return count
