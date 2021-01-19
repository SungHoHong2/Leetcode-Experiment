class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # set the hashmap to build an undirected graph
        self.graph = collections.defaultdict(list)
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
        # set the hashmap to record the minimum rank that the nodes can reach
        self.lowestRank = collections.defaultdict(int)
        # set the table to mark the visited nodes
        self.visited = set()
        # return the critical edges from the dfs (rank, prev, src)
        return self.dfs(0, -1, 1)

    def dfs(self, rank, prev, src):
        # set the list for returning the critical edges
        ans = list()
        # mark the node as visited
        self.visited.add(src)
        # set the minimum rank
        self.lowestRank[src] = rank
        # explore the neighbors
        for dest in self.graph[src]:
            # if the vertex is not visited
            if dest not in self.visited:
                # combine the returning edges by exploring the neighbors with dfs
                ans += self.dfs(rank + 1, src, dest)
            # if the node did not reach the deadend
            if prev != dest:
                # update the lowest rank reachable once formed a cycle
                self.lowestRank[src] = min(self.lowestRank[src], self.lowestRank[dest])
                # append the edge as the critical if the edge does not return as a cycle
                if rank < self.lowestRank[dest]:
                    ans.append([src, dest])
        # return the critical edges
        return ans