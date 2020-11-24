class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # append all unique letters into the adjacency list
        adj_list = {c : [] for word in words for c in word}
        # iterate each pair of adjacent words
        for first_word, second_word in zip(words, words[1:]):
            # iterate each pair of characters from the adjacent words
            for c, d in zip(first_word, second_word):
                # if the character is different
                if c != d:
                    # append to the adjacency list
                    adj_list[d].append(c)
                    break
            # return empty string if the second word is a subset of the first word
            else:
                if len(second_word) < len(first_word):
                    return ""
        # set a hashmap to check the visited nodes
        seen = {} # False = grey, True = black.
        # set the list to collect the order of characters
        output = []
        # run DFS
        def visit(node):
            # return the result of the visited node
            if node in seen:
                return seen[node]
            # mark the node as grey
            seen[node] = False
            # explore the adjacent nodes and return False if the cycle is detected
            for next_node in adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False
            # mark the node as black
            seen[node] = True # Mark node as black.
            # append the result
            output.append(node)
            # return True
            return True
        # if all the nodes return true
        if not all(visit(node) for node in adj_list):
            return ""
        return "".join(output)