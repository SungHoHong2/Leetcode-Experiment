class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # get the length of the word1
        n = len(word1)
        # get the length of the word2
        m = len(word2)
        # return the total length of a word if one of the word is empty
        if n * m == 0:
            return n + m
        # set a dp table
        dp = [ [0 for _ in range(m + 1)] for _ in range(n + 1)]
        # update the number of changes for word1
        for i in range(n + 1):
            dp[i][0] = i
        # update the number of changes for word2
        for j in range(m + 1):
            dp[0][j] = j
        # iterate the dp for word1
        for i in range(1, n + 1):
            # iterate the dp for wrod2
            for j in range(1, m + 1):
                # case1: get the minimum number of changes for word1 to become word2
                down = dp[i - 1][j] + 1
                # case2: get the minimum number of changes for word2 to become word1
                left = dp[i][j - 1] + 1
                # case3: get the minimum number of changes for before word1 and word2 changes
                diagonal = dp[i - 1][j - 1]
                # increase the number of changes for case3 if word1 and word2 are not equal
                if word1[i - 1] != word2[j - 1]:
                    diagonal += 1
                # update the minimum number of changes for word1 and word2 become equal
                dp[i][j] = min(left, down, diagonal)
        # return the minimum number of changes
        return dp[n][m]