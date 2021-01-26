class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        qo = collections.deque([(0, 0, 0)])
        qt = collections.deque([(x, y, 0)])
        do, dt = {(0,0): 0}, {(x,y): 0}
        while True:
            ox, oy, ostep = qo.popleft()
            if (ox, oy) in dt: return ostep + dt[(ox, oy)]
            tx, ty, tstep = qt.popleft()
            if (tx, ty) in do: return tstep + do[(tx, ty)]
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]:
                if (ox+dx, oy+dy) not in do and -1 <= ox+dx <= x+2 and -1 <= oy+dy <= y+2:
                    qo.append((ox+dx, oy+dy, ostep+1))
                    do[(ox+dx,oy+dy)] = ostep+1
                if (tx+dx, ty+dy) not in dt and -1 <= tx+dx <= x+2 and -1 <= ty+dy <= y+2:
                    qt.append((tx+dx, ty+dy, tstep+1))
                    dt[(tx+dx,ty+dy)] = tstep+1
        return -1