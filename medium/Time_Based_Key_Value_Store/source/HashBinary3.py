class TimeMap:
    def __init__(self):
        # initialize a map that uses the list as a value
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append the key and the value
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # return an emtpy string if there is a key in the hashmap
        if key not in self.hashmap:
            return ""
        # get the history of the key
        array = self.hashmap[key]
        # set the pointers for binary search
        left, right = 0, len(self.hashmap[key]) - 1
        # return empty if the earliest history is later than the requested timestamp
        if array[left][0] > timestamp:
            return ""
        # return the latest history if it is earlier than the requested timestamp
        if array[right][0] <= timestamp:
            return array[right][1]
        # start binary search
        while left <= right:
            # get the pivot
            mid = (left + right) // 2
            # return the pivot if it equals to the timestamp
            if array[mid][0] == timestamp:
                return array[mid][1]
            # explore the leftside if the timestamp is larger than the pviot
            if array[mid][0] < timestamp:
                left = mid + 1
            # explore the rightside if the timestamp is smaller than the pivot
            else:
                right = mid - 1
        # return the value of the right index
        return array[right][1]
