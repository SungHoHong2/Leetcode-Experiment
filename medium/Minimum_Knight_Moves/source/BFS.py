class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # create a BFS queue that contains (x,y,steps)
        q = collections.deque()
        # append the original position with zero steps
        q.append((0,0,0))
        # set a hashmap for visited
        visited = set([(0,0)])
        # loop until the queue is depleted
        while q:
            # pop the position and the steps
            a, b, step = q.popleft()
            # return the number of steps if it is equal to the destination
            if (a, b) == (x,y):
                return step
            # search the direction
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1), (-1, -2), (-2,-1)]:
                # if the destination is unvisited and the index is within the boundaries
                if (a+dx, b+dy) not in visited:
                    # mark the position to the visited
                    visited.add((a+dx, b+dy))
                    # append the position and increase the number of steps
                    q.append((a+dx, b+dy, step+1))
        # return -1 if BFS fails to reach the destination
        return -1