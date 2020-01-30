class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rdict = {}
        self.rlist = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.rdict:
            return False
        self.rdict[val] = len(self.rlist)
        self.rlist.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.rdict:
            # move the last element to the place idx of the element to delete
            # remove c
            # 1 2 3 4 5
            # a b c d e

            last_element = self.rlist[-1]
            # 1 2 3 4 [5]
            # a b c d  e

            idx = self.rdict[val]
            # 1 2  3  4 5
            # a b [c] d e

            # override the last element to the current position of the array
            self.rlist[idx] = last_element
            # 1 2  3  4 5
            # a b [e] d e

            # update the dictionary of the last element with the current index
            self.rdict[last_element] = idx

            # delete the last element
            self.rlist.pop()
            del self.rdict[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.rlist)

