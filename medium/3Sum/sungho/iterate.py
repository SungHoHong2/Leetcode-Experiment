class Solution(object):

    def threeSum(self, nums):
        res = []

        # First, we sort the array, so we can easily move i around and know how to adjust l and r.
        nums.sort()
        length = len(nums)

        for i in range(0, length - 2):

            # We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero.
            if nums[i] > 0:
                break

                # If the number is the same as the number before, we have used it as target already, continue.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # We always start the left pointer from i+1 because the combination of 0~i has already been tried
            l, r = i + 1, length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # If the total is less than zero, we need it to be larger, so we move the left pointer.
                if total < 0:
                    l += 1

                # If the total is greater than zero, we need it to be smaller, so we move the right pointer.
                elif total > 0:
                    r -= 1

                # If the total is zero, bingo!
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # We need to move the left and right pointers to the next different numbers, so we do not get repeating result.
                    while l < r and nums[l] == nums[l + 1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res