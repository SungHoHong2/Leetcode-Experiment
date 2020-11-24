from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # set a hashmap accepting set as a value
        adj_list = defaultdict(set)
        # set a hashmap to track of the number of incoming nodes
        in_degree = {c : 0 for word in words for c in word}
        # iterate each pair of adjacent words
        for first_word, second_word in zip(words, words[1:]):
            # iterate each pair of characters from the adjacent words
            for c, d in zip(first_word, second_word):
                # if the character is different
                if c != d:
                    # if the character from the second word is not part of the adjacency hashmap
                    if d not in adj_list[c]:
                        # store the character in the adjacency list
                        adj_list[c].add(d)
                        # increase the number of incoming nodes
                        in_degree[d] += 1
                    break
            # return empty string if the second word is a subset of the first word
            else:
                if len(second_word) < len(first_word): return ""
        # set the list to collect the order of characters
        output = []
        # create a double ended queue and add the starting nodes
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        # run the BFS and append the order of characters
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # return the empty string if there are missing characters in the result
        if len(output) < len(in_degree):
            return ""
        # return the result as a string
        return "".join(output)