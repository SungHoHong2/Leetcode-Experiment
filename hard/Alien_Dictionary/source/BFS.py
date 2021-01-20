class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # set a hashmap accepting set as a value
        adj_list = {c : list() for word in words for c in word}
        # iterate each pair of adjacent words
        for first, second in zip(words, words[1:]):
            # set a flag to check if the neighbors are identical
            identical = True
            # iterate each pair of characters from the adjacent words
            for src, dest in zip(first, second):
                # if the character is different
                if src != dest:
                    # store the character in the adjacency list
                    adj_list[dest].append(src)
                    # mark as identical found
                    identical = False
                    # break because there is no way to identify the order beyond this
                    break
            # return empty string if the second word is a subset of the first word
            if identical and len(second) < len(first):
                return ""
        # set a hashmap to check the visited nodes
        seen = dict() # False = grey, True = black.
        # set the list to collect the order of characters
        output = list()
        # run the DFS
        def dfs(dest):
            # return the result of the visited node
            if dest in seen:
                return seen[dest]
            # mark the node as grey
            seen[dest] = False
            # explore the adjacent nodes and return False if the cycle is detected
            for src in adj_list[dest]:
                if not dfs(src):
                    return False
            # mark the node as black if there is no cycle or the node is a single
            seen[dest] = True
            # append the result
            output.append(dest)
            # return True
            return True
        # return empty if one of the dfs returns False
        if not all(dfs(node) for node in adj_list.keys()):
            return ""
        # return the order of the characters as a string
        return "".join(output)