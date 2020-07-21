class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        record = defaultdict(int)
        for num in nums:
            record[num] += 1

            # sort the repeated numbers in reverse
        history = None
        if len(record.items()) > 0:
            history = [(key, val) for key, val in record.items()]
            history.sort(key=lambda x: x[1])
            history.reverse()

        # collect the most repeated numbers
        if len(history) > 0:

            for i in range(1, len(history)):
                if history[i][1] != history[0][1]:
                    history = history[0:i]
                    break

        history = [hist[0] for hist in history]

        # find the shortest subset possible for the repeated numbers
        shortest = list()
        for hist in history:
            length = list()
            for i in range(len(nums)):
                if nums[i] == hist:
                    length.append(i)

            if len(length) > 1:
                shortest.append(length[-1] - length[0])

        # get the shortest length
        shortest.sort()

        if len(shortest) > 0:
            return shortest[0] + 1
        else:
            return 1