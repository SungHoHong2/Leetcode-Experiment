class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # set the BFS queue that starts from the origin
        qo = collections.deque([(0, 0, 0)])
        # set the BFS queue that starts from the destination
        qt = collections.deque([(x, y, 0)])
        # set visited hashmap for both BFS queues
        do, dt = {(0,0): 0}, {(x,y): 0}
        # iterate
        while qo and qt:
            # pop the position from the first queue
            ox, oy, ostep = qo.popleft()
            # return the steps if first BFS meets the second BFS
            if (ox, oy) in dt:
                return ostep + dt[(ox, oy)]
            # pop the position from the second queue
            tx, ty, tstep = qt.popleft()
            # return the steps if second BFS meets the first BFS
            if (tx, ty) in do:
                return tstep + do[(tx, ty)]
            # iterate the possible directions
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]:
                # append the unvisited positions and increase the steps of the first BFS
                if (ox+dx, oy+dy) not in do :
                    qo.append((ox+dx, oy+dy, ostep+1))
                    do[(ox+dx,oy+dy)] = ostep+1
                # append the unvisited positions and increase the steps of the second BFS
                if (tx+dx, ty+dy) not in dt :
                    qt.append((tx+dx, ty+dy, tstep+1))
                    dt[(tx+dx,ty+dy)] = tstep+1
        # return -1 if BFS fails to reach the destination
        return -1