class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # create a BFS queue that contains (x,y,steps)
        q = collections.deque()
        # append the original position with zero steps
        q.append((0,0,0))
        # set the destination to absolute to reduce the searching space
        x, y = abs(x), abs(y)
        # set a hashmap for visited
        visited = set([(0,0)])
        # loop until the queue is depleted
        while q:
            # pop the position and the steps
            a, b, step = q.popleft()
            # return the number of steps if it is equal to the destination
            if (a, b) == (x,y): return step
            # search the direction except (-1, -2) and (-2, -1) since the destination is absolute
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:
                # if the destination is unvisited and the index is within the reduced search space
                if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                    # mark the position to the visited
                    visited.add((a+dx, b+dy))
                    # append the position and increase the number of steps
                    q.append((a+dx, b+dy, step+1))
        # return -1 if BFS fails to reach the destination
        return -1