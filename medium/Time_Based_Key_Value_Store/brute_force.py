class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        prev = None

        if key in self.map:
            for item in self.map[key]:
                # print(item)
                if item[1] == timestamp:
                    return item[0]

                if item[1] < timestamp:
                    prev = item[0]

            # print(self.map[key][-1])
            if timestamp < self.map[key][0][1]:
                return ""

            if prev:
                return prev

            return self.map[key][-1][0]

        return None
