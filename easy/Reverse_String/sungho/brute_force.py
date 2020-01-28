class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        temp = s[::-1]
        for i in range(len(temp)):
            s[i] = temp[i]
