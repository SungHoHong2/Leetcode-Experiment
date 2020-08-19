class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        result = sorted(list(intervals))
        # set a flag for merge
        has_merge = True
        # loop until there is no intervals to merge
        while has_merge:
            # set the merge flag to false
            has_merge = False
            # compare all the intervals
            for i in range(len(result)-1):
                # if there is a merge break
                if has_merge:
                    break
                for j in range(i+1, len(result)):
                    # get the interval from i
                    a = result[i]
                    # get the interval from j
                    b = result[j]
                    # check if the two intervals overlap
                    if not (a[1] < b[0] or a[0] > b[1] or b[0] > a[1] or b[1] < a[0]):
                        # merge interval to i
                        result[i] = [min(a[0], b[0]), max(a[1], b[1])]
                        # remove the interval of j
                        result.pop(j)
                        # set the merge flag to true
                        has_merge = True
                        # break
                        break
        # return the result
        return result