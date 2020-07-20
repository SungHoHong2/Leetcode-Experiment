class Bucket:
    def __init__(self):
        # initialize a list
        self.bucket = []

    def get(self, key):
        # iterate the list
        for (k, v) in self.bucket:
            # if key is found in the list
            if k == key:
                # return the value
                return v

        # if not return -1
        return -1

    def update(self, key, value):

        # initiate the found flag
        found = False

        # iterate the list
        for i, kv in enumerate(self.bucket):
            # if the key exists in the list
            if key == kv[0]:
                # update the existing key
                self.bucket[i] = (key, value)
                # set the found to true
                found = True
                break

        # if key does not exist in the list
        if not found:
            # add new value
            self.bucket.append((key, value))

    def remove(self, key):
        # iterate the list
        for i, kv in enumerate(self.bucket):
            # if key is found
            if key == kv[0]:
                # delete from the list
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        # create the number of lists for the hash table
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        # use modulo as a hash function
        hash_key = key % self.key_space
        # get the list that corresponds with the hash_key and update
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        # use modulo as a hash function
        hash_key = key % self.key_space
        # get the list that corresponds with the hash_key and get the value
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """

        # use modulo as a hash function
        hash_key = key % self.key_space
        # get the list that corresponds with the hash_key and remove the value
        self.hash_table[hash_key].remove(key)
