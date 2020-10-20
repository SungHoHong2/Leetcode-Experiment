class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # set the map for tracking the results of the subproblems
        dp = {}
        # set the variable to return the number of possible chains
        result = 1
        # sort the words by length
        words = sorted(words, key=len)
        # iterate the words
        for word in words:
            # store the current word as a key
            dp[word] = 1
            for i in range(len(word)):
                # generate a word that excludes the ith index
                prev = word[:i] + word[i + 1:]
                # if the generated word exists in the map
                if prev in dp:
                    # update the possible chain of the current word
                    dp[word] = max(dp[prev] + 1, dp[word])
                    # keep track of the maximum length of the chain
                    result = max(result, dp[word])
        # return the maximum length of the chain
        return result