# For each key we get or set, we only care about the timestamps and values for that key. We can store this information in a HashMap.
# Now, for each key, we can binary search the sorted list of timestamps to find the relevant value for that key.

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key, None)
        if A is None: return ""
        # bisect function returns the position in the sorted list
        i = bisect.bisect(A, (timestamp, chr(127)))

        # get the result from the previous timestamp
        return A[i - 1][1] if i else ""