class Solution:
    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set the table of parents for the disjoint set
        parents = [i for i in range(len(adjacency))]
        # set the table of ranking for the disjoint set
        ranking = [1 for i in range(len(adjacency))]

        def getParent(i):
            # set the temporary pointer just in case the current node already has a parent
            j = i
            # if the selected node already has a parent
            if parents[j] != j:
                # get the address of the parent
                j = parents[j]
                # update the parent table of that node
                parents[i] = parents[j]
            # return the index of the parent
            return parents[i]

        def setParent(curr, parent):
            # store the parent address to the current cell
            parents[curr] = parent

        def getRank(parent):
            # return the rank from the table
            return ranking[parent]

        def setRank(parent, rank):
            # update the rank
            ranking[parent] = rank

        def union(a, b):
            # get the parents of both 'a' and 'b'
            p_a, p_b = getParent(a), getParent(b)
            # return the ranks of both 'a' and 'b'
            rank_a, rank_b = getRank(p_a), getRank(p_b)
            # if the rank of the 'b' is higher
            if rank_a < rank_b:
                # set the parent of 'a' to parent of 'b'
                setParent(p_a, p_b)
            # if the rank of the 'a' is higher
            elif rank_a > rank_b:
                # set the parent of 'b' to parent of 'a'
                setParent(p_b, p_a)
            # if the ranks of 'a' and 'b' are the same
            else:
                # increase the number of rank and merge the group
                setParent(p_b, p_a)
                setRank(p_a, rank_a + 1)

                # iterate the number of nodes

        for i in range(len(adjacency)):
            # iterate the neighbors
            for j, con in enumerate(adjacency[i]):
                # if the neighbor is valid
                if con == 1:
                    # merge two provinces
                    union(i, j)

        # count the number of provinces that has the parent as itself
        provinces = 0
        for i in range(len(adjacency)):
            if i == getParent(i):
                provinces += 1

                # return the total number of provinces
        return provinces