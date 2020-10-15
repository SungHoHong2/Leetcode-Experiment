class TimeMap:
    def __init__(self):
        # initialize a map that uses the list as a value
        self.M = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append the key and the value
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # return empty string if the key is not in the map
        A = self.M.get(key, None)
        if A is None: return ""
        # bisect.bisect function to return the position of requested timestamp in the sorted list (Note that bisect requires the list to be already sorted)
        i = bisect.bisect(A, (timestamp, chr(127)))
        # return the result of the value if not return empty string
        return A[i - 1][1] if i else ""