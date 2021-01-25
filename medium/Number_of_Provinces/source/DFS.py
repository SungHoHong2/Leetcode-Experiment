class Solution:

    def dfs(self, i):
        # return if province is out of range or already visited
        if not (0 <= i < len(self.adjacency)) or self.visited[i]:
            return
            # mark the province as visited
        self.visited[i] = 1
        # iterate the neighbors
        for j, adj in enumerate(self.adjacency[i]):
            # if the neighbors are connected
            if adj == 1:
                # run the dfs
                self.dfs(j)

    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set a adjacency table as global
        self.adjacency = adjacency
        # set the visited table
        self.visited = [0 for _ in range(len(adjacency))]
        # set the total number of provinces
        provinces = 0
        # iterate the provinces
        for i in range(len(adjacency)):
            # if the province is not visited
            if not self.visited[i]:
                # increase the number of province
                provinces += 1
                # run the dfs
                self.dfs(i)
        # return the total number of provinces
        return provinces