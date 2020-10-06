class Solution(object):
    def groupAnagrams(self, strs):
        # create a map which uses the value as a list
        ans = collections.defaultdict(list)
        # iterate the strings
        for s in strs:
            # save the sorted string as the key and add the string to the list
            ans[tuple(sorted(s))].append(s)
        # return the grouped values
        return ans.values()