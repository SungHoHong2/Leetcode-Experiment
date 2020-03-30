# For each key we get or set, we only care about the timestamps and values for that key. We can store this information in a HashMap.
# Now, for each key, we can binary search the sorted list of timestamps to find the relevant value for that key.

class TimeMap(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""