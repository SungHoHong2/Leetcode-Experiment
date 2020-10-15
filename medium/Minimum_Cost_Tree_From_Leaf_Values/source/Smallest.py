class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # set the variable to return the sum of non-leaf nodes
        res = 0
        # loop until the array is depleted
        while len(arr) > 1:
            # get the index of the smallest element in the array
            i = arr.index(min(arr))
            # get the neighboring leaves of the smallest leaf
            neighbors = arr[i - 1:i] + arr[i + 1:i + 2]
            # pop the smallest leaf
            smallest = arr.pop(i)
            # create the parent by multiplying the smallest with the smallest neighboring leaf
            res += min(neighbors) * smallest
        return res