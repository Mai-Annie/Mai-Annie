class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = grid
        
        #Create 2D array for columns by doing the transpose of the grid
        columns = [[0] * len(grid) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                columns[j][i] = grid[i][j]

        #Count how many rows/columns are equal
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if rows[i] == columns[j]:
                    counter += 1
        
        return counter
        

        