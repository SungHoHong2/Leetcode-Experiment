class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up a queue for bfs
        queue = list()
        # set the record of visited for the substrings
        visited = [False for i in range(len(s))]
        # append the queue with the starting point zero
        queue.append(0)
        # loop until the queue is depleted
        while queue:
            # pop the next beginning index of the substring
            start = queue.pop()
            # if the substring is not visited
            if not visited[start]:
                # iterate the substring
                for end in range(start+1,len(s)+1):
                    # if the substring is part of the wordDict
                    if s[start:end] in wordDict:
                        # append the the end index to the queue
                        queue.append(end)
                        # if end index reached the final index of the string
                        if end == len(s):
                            # return true
                            return True
                # record the substring as visited
                visited[start] = True
        # return false if there are no branches that will create all valid substrings
        return False