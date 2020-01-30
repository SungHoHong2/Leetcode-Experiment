class RandomizedSet:

    def __init__(self):
        self.rdict = {}
        self.rlist = []

    def insert(self, val: int) -> bool:
        # if there is nothing in the dictionary return false
        if val in self.rdict:
            return False

        # add the element to the hashmap as (value, index)
        self.rdict[val] = len(self.rlist)

        # append to the array
        self.rlist.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        # if the value is in the hashmap
        if val in self.rdict:
            # purpose is to override the target element with the last element

            # get the value of last element from the array
            last_element = self.rlist[-1]
            # 1 2 3 4  5
            # a b c d [e]

            # get the index of the target element
            idx = self.rdict[val]
            # 1 2  3  4 5
            # a b [c] d e

            # override the target element with the last element in the array
            self.rlist[idx] = last_element
            # 1 2  3  4 5
            # a b [e] d e

            # override the target element with the last element in the hashmap
            self.rdict[last_element] = idx

            # delete the last element in the array
            self.rlist.pop()
            # delete the element in the hashmap
            del self.rdict[val]
            return True

        return False

    def getRandom(self) -> int:
        # return random choice
        return random.choice(self.rlist)

