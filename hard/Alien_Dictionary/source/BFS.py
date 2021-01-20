from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # set a hashmap accepting set as a value
        adj_list = defaultdict(set)
        # set a hashmap to track of the number of incoming nodes for each char
        incoming = {char : 0 for word in words for char in word}
        # iterate each pair of adjacent words
        for first, second in zip(words, words[1:]):
            # set a flag to check if the neighbors are identical
            identical = True
            # iterate each pair of characters from the adjacent words
            for src, dest in zip(first, second):
                # if the character is different
                if src != dest:
                    # if the character from the second word is not part of the adjacency hashmap
                    if dest not in adj_list[src]:
                        # store the character in the adjacency list
                        adj_list[src].add(dest)
                        # increase the number of incoming nodes
                        incoming[dest] += 1
                    # mark as identical found
                    identical = False
                    # break because there is no way to identify the order beyond this
                    break
            # if all the compared words are identical
            if identical:
                # return empty string if the second word is a subset of the first word
                if len(second) < len(first):
                    return ""
        # set the list to collect the order of characters
        output = list()
        # create a BFS queue that contains nodes without incomming nodes
        queue = deque([src for src in incoming if incoming[src] == 0])
        # run the BFS
        while queue:
            # pop out the node
            src = queue.popleft()
            # append as the answer
            output.append(src)
            # explore the destinations of the current node
            for dest in adj_list[src]:
                # decrease the incomming node of the destination
                incoming[dest] -= 1
                # append the dest to the BFS queue if the number of incomming nodes is zero
                if incoming[dest] == 0:
                    queue.append(dest)
        # return the empty string if there are disconnected graphs
        if len(output) < len(incoming):
            return ""
        # return the order of the characters as a string
        return "".join(output)