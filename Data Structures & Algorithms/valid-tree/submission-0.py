class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False

        treeMap = {node:[] for node in range(n)}

        for l, r in edges:
            treeMap[l].append(r)
            treeMap[r].append(l)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in treeMap[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False
            
            return True

        res = dfs(0, -1)

        if len(visited) != n:
            return False
        
        return res