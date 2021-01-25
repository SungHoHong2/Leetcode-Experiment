class Solution:

    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set the total number of provinces
        provinces = 0
        # set a hashset that stores the unvisited provinces
        unvisited = set([i for i in range(len(adjacency))])
        # set the queue for BFS
        queue = collections.deque()
        # loop until all the unvisited provinces are explored
        while unvisited:
            # pop and append one of the unvisited provinces to the queue
            queue.append(unvisited.pop())
            # increase the number of province
            provinces += 1
            # loop until the queue is empty
            while queue:
                # pop a province from the queue
                i = queue.pop()
                # iterate its neighbors
                for j, edge in enumerate(adjacency[i]):
                    # if the neighbor is connected and unvisited
                    if edge == 1 and j in unvisited:
                        # append the neighbor to the queue
                        queue.append(j)
                        # remove the neighbor from the unvisited provinces
                        unvisited.remove(j)
        # return the total number of provinces
        return provinces