class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0

        # run until all the elements in the array is depleted
        while len(arr) > 1:
            # get the index of the smallest element in the array
            i = arr.index(min(arr))

            # get the next smallest element and multiply with the smallest element
            print('before', min(arr), i, arr[i - 1:i] + arr[i + 1:i + 2],
                  min(arr) * min(arr[i - 1:i] + arr[i + 1:i + 2]) + res)
            res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)

        return res