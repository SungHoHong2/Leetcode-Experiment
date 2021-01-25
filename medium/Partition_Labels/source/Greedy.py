class Solution(object):
    def partitionLabels(self, S):
        # create a hashmap that collects the rightmost index of the character
        rightmost = {c: i for i, c in enumerate(S)}
        # set the index that records the rightmost index and the next starting point
        right = start = 0
        # set the returning array
        ans = []
        # iterate the input
        for i, c in enumerate(S):
            # record the maximum rightmost index
            right = max(right, rightmost[c])
            # if the rightmost index equals to the current index
            if i == right:
                # append the length of the shortest substring
                ans.append(i - start + 1)
                # mark the starting point of the next substring
                start = i + 1
        # return the lengths of the partitoined substrings
        return ans