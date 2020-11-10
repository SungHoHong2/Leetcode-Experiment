class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # set the hashamp for storing the edges
        self.graph = collections.defaultdict(list)
        ## set the pointer for tracking the order of current rank
        rank = 0
        # set the hashamp to record the minimum rank that the nodes can reach
        self.lowestRank = collections.defaultdict(int)
        # set the table to mark the visited nodes
        self.visited = [False for _ in range(n)]
        ## build graph using the hashmap
        for connection in connections:
            self.graph[connection[0]].append(connection[1])
            self.graph[connection[1]].append(connection[0])
        # set the list for returning the critical edges
        res = []
        # set the pointer for the previous vertex
        prev = -1
        # set the pointer for the current vertex
        current = 0
        # start the dfs
        self.dfs(res, rank, prev, current)
        # return the critical edges
        return res

    def dfs(self, res, rank, prev, current):
        print('dfs', {'current': current, 'rank': rank})
        # mark the node as visited
        self.visited[current] = True
        # set the minimum rank
        self.lowestRank[current] = rank
        # explore the neighbors
        for next in self.graph[current]:
            # if the vertex is not visited
            if not self.visited[next]:
                # explore the neighbors with dfs
                # print('explored',{'current': current, 'next':next, 'rank': rank })
                self.dfs(res, rank + 1, current, next)
            # do not go to the previous vertex
            if next != prev:
                # print('update',{'current':(current,self.lowestRank[current]), 'next':(next ,self.lowestRank[next])})
                # update the lowest rank reachable
                self.lowestRank[current] = min(self.lowestRank[current], self.lowestRank[next])
                # the edge is not the cycle if the current rank is no longer compatible with the lowest reachable rank
                if self.lowestRank[next] >= rank + 1:
                    res.append([current, next])