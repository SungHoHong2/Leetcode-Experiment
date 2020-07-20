### House Robber

- **Dynamic Programming**
    - [concepts](image/dp.png)
    - [source code](source/dp.py)
    
    
    
     def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def ismagic(grid, x, y):
            flat = [grid[x+i][y+j] for i in (-1, 0, 1) for j in (-1, 0, 1)]
            if set(flat) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            if any([sum(grid[x+i][y+j] for j in (-1, 0, 1)) != 15 for i in (-1, 0, 1)]):
                return False
            if any([sum(grid[x+i][y+j] for i in (-1, 0, 1)) != 15 for j in (-1, 0, 1)]):
                return False
            if sum(grid[x-i][y-i] for i in (-1, 0, 1)) != 15 or sum(grid[x+i][y-i] for i in (-1, 0, 1)) != 15:
                return False
            return True
        
        rst = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if ismagic(grid, i, j):
                    rst += 1
        return rst
        