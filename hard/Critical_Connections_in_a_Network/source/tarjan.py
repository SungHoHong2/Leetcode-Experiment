class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # set the hashmap for storing the list of undirected src and dests
        self.graph = collections.defaultdict(list)
        # set the pointer for tracking the order of discovery
        rank = 0
        # set the hashmap to record the minimum rank that the nodes can reach
        self.lowestRank = collections.defaultdict(int)
        # set the table to mark the visited nodes
        self.visited = [False for _ in range(n)]
        # build an undirected graph
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
        # set the list for returning the critical edges
        res = list()
        # set the pointer for the previous vertex
        prev = -1
        # set the pointer for the current vertex
        current = 0
        # start the dfs
        self.dfs(res, rank, prev, current)
        # return the critical edges
        return res

    def dfs(self, res, rank, prev, current):
        # mark the node as visited
        self.visited[current] = True
        # set the minimum rank
        self.lowestRank[current] = rank
        # explore the neighbors
        for next in self.graph[current]:
            # if the vertex is not visited
            if not self.visited[next]:
                # explore the neighbors with dfs
                self.dfs(res, rank + 1, current, next)
            # if the node did not reach the deadend
            if next != prev:
                # update the lowest rank reachable once formed a cycle
                self.lowestRank[current] = min(self.lowestRank[current], self.lowestRank[next])
                # add critical edge if the edge does not return as a cycle
                if self.lowestRank[next] > rank:
                    res.append([current, next])
