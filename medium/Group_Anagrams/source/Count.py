class Solution:
    def groupAnagrams(strs):
        # create a map that uses values as a list
        ans = collections.defaultdict(list)
        # iterate the string
        for s in strs:
            # create a array of alphebatical order
            count = [0] * 26
            # iterate the string
            for c in s:
                # count the number of each character
                count[ord(c) - ord('a')] += 1
            # store the number of the count as the key and append the string as a value
            ans[tuple(count)].append(s)
        # return the result
        return ans.values()