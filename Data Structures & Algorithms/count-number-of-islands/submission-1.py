class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] == "0"):
                return

            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                bfs(row + 1, col)
                bfs(row - 1, col)
                bfs(row, col - 1)
                bfs(row, col + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands