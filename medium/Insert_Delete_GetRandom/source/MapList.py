class RandomizedSet:

    def __init__(self):
        # set up the map
        self.hashmap = dict()
        # set up the list
        self.array = list()

    def insert(self, val: int) -> bool:
        # return false if the inserted item is already in the hashmap
        if val in self.hashmap:
            return False
        # add key as the inserted item and value as the future index of the array to the hashmap
        self.hashmap[val] = len(self.array)
        # append inserted item to the array
        self.array.append(val)
        # return true
        return True

    def remove(self, val: int) -> bool:
        # if the item is in the hashmap
        if val in self.hashmap:
            # get the latest item appended in the array
            latest_val = self.array[-1]
            # get the index of the removing item
            removing_index = self.hashmap[val]
            # override the removing item with the latest item in the array
            self.array[removing_index] = latest_val
            # update latest item in the map with the index of the removing item
            self.hashmap[latest_val] = removing_index
            # delete the latest index in the array
            self.array.pop()
            # delete the removing item in the map
            del self.hashmap[val]
            # return true
            return True
        # return false if there is no item in the hashmap
        return False

    def getRandom(self) -> int:
        # use the built-in random.choice function to return the item from the list
        return random.choice(self.array)