class RandomizedSet:

    def __init__(self):
        # set up the map
        self.rdict = {}
        # set up the list
        self.rlist = []

    def insert(self, val: int) -> bool:
        # if the inserted item is already in the map
        if val in self.rdict:
            # return false
            return False
        # add key as the inserted item and the total length of the list as the value to the map
        self.rdict[val] = len(self.rlist)
        # append to inserted item to the list
        self.rlist.append(val)
        # return true
        return True

    def remove(self, val: int) -> bool:
        # if the item is in the hashmap
        if val in self.rdict:
            # get the latest item appended in the list
            last_element = self.rlist[-1]
            # get the index of the removing item
            idx = self.rdict[val]
            # override the removing item with the latest item in the list and the map
            self.rlist[idx] = last_element
            self.rdict[last_element] = idx
            # delete the lastest index in the array
            self.rlist.pop()
            # delete the removing item in the map
            del self.rdict[val]
            # return true
            return True
        # return false
        return False

    def getRandom(self) -> int:
        # use the built-in random.choice function to return the item from the list
        return random.choice(self.rlist)