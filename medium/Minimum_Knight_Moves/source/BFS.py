class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)])
        x, y, visited = abs(x), abs(y), set([(0,0)])
        while q:
            a, b, step = q.popleft()
            if (a, b) == (x,y): return step
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:  # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
                if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                    visited.add((a+dx, b+dy))
                    q.append((a+dx, b+dy, step+1))
        return -1 