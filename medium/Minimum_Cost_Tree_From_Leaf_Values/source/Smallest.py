class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # set the variable to return the sum of non-leaf nodes
        ans = 0
        # loop until the array is depleted
        while arr :
            # get the index of the smallest element in the array
            i = arr.index(min(arr))
            # get the neighboring leaves of the smallest leaf
            neighbors = arr[i - 1:i] + arr[i + 1:i + 2]
            # pop the smallest leaf
            smallest = arr.pop(i)
            # accumulate the result by multiplying the smallest with the smallest neighboring leaf
            ans += min(neighbors) * smallest if neighbors else 0
        # return the accumulated result
        return ans