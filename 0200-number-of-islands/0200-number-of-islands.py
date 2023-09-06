class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            if (
                0 <= i < len(grid) and
                0 <= j < len(grid[0]) and
                grid[i][j] == '1'
            ):
                grid[i][j] = '0'  # Mark the land cell as visited
                dfs(i + 1, j)  # Explore down
                dfs(i - 1, j)  # Explore up
                dfs(i, j + 1)  # Explore right
                dfs(i, j - 1)  # Explore left

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)  # Start DFS to explore the island

        return num_islands
