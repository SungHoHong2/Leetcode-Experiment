class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        list1 = [i for i in s]
        list2 = [i for i in t]

        list1.sort()
        list2.sort()

        if list1 == list2:
            return True
        else:
            return False
