class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr) - 1

            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:

            i = self.dict[val]
            last = self.arr[-1]
            self.dict[last] = i
            self.arr[i] = last
            self.arr.pop()
            del self.dict[val]

            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand = random.randrange(0, len(self.arr), 1)
        return self.arr[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()