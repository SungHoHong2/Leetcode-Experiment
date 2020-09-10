class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a hashmap
        hashmap = {}
        # set the variables for counter and the sum
        count, sum = 0, 0
        # count zero in hashmap
        hashmap[0] = 1
        # iterate the numbers
        for i in nums:
            # accumulate the sum
            sum += i
            # if the sum subtracted from k is found in hashmap
            if ((sum - k) in hashmap):
                # subarray sum of k exists so increase the number of counts
                count += hashmap[sum - k]
            # if the sum is found again in the hashmap
            if (sum in hashmap):
                # increase the number of counts
                hashmap[sum] += 1
            # if the sum does not exist in the hashmap
            else:
                # start counting the sum in hashmap
                hashmap[sum] = 1
        # return the number of counts
        return count


