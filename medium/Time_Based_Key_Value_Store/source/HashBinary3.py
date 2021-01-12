class Node:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value

class TimeMap:
    def __init__(self):
        # initialize a map that uses the list as a value
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append the key and the value
        self.hashmap[key].append(Node(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # return an emtpy string if there is a key in the hashmap
        if key not in self.hashmap:
            return ""
        # get the history of the key
        history = self.hashmap[key]
        # set the pointers for binary search
        left, right = 0, len(history) -1
        # return empty if the earliest history is later than the requested timestamp
        if history[0].timestamp > timestamp:
            return ""
        # return the latest history if it is earlier than the requested timestamp
        if history[-1].timestamp < timestamp:
            return history[-1].value
        # start binary search
        while left <= right:
            # get the pivot
            pivot = (left + right) // 2
            # return the pivot if it equals to the timestamp
            if history[pivot].timestamp == timestamp:
                return history[pivot].value
            # explore the rightside if the timestamp is larger than the pivot
            if history[pivot].timestamp < timestamp:
                left = pivot + 1
            # explore the leftside if the timestamp is smaller than the pivot
            else:
                right = pivot - 1
        # return the value of the right index
        return history[right].value