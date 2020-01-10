class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = sorted(list(intervals))

        has_merge = True
        while has_merge:
            i = 0
            has_merge = False

            while i < len(result) and not has_merge:

                # try to merge i with j
                j = 0
                while j < len(result) and not has_merge:
                    if i != j:
                        a = result[i]
                        b = result[j]

                        # check if a & b is overlap
                        if not (a[1] < b[0] or a[0] > b[1] or b[0] > a[1] or b[1] < a[0]):
                            # merge to i
                            result[i] = [min(a[0], b[0]), max(a[1], b[1])]
                            result.pop(j)

                            has_merge = True

                    j += 1

                i += 1

        return result