class Window:
    def __init__(self, length, left, right):
        self.length = length
        self.left = left
        self.right = right

class Solution:
    def minWindow(self, s, t):
        # return empty string if the input is invalid
        if not t or not s:
            return ""
        # set a hashmap that counts the frequency of the unqiue characters of the target
        target_count = collections.defaultdict(int)
        for c in t:
            target_count[c] += 1
        # get the total number of unique characters of the target
        required = len(target_count)
        # left and right pointer
        l, r = 0, 0
        # keep track of number of characters of target that are matched with input
        formed = 0
        # set a hashmap that counts the frequency of the unqiue characters of the current window
        window_count = collections.defaultdict(int)
        # set a returning tuple (window length, left, right)
        ans = Window(float("inf"), None, None)
        # start expanding the window from the right
        for r in range(len(s)):
            # get the new character from the right
            character = s[r]
            # add to the map
            window_count[character] += 1
            # check if the frequency of the character in the window matchs with the target
            if character in target_count and window_count[character] == target_count[character]:
                formed += 1
            # start shrinking the window from the left once it contains the substring of the target
            while l <= r and formed == required:
                # get the old character from the left
                character = s[l]
                # record the smallest window
                if r - l + 1 < ans.length:
                    ans.length = r - l + 1
                    ans.left, ans.right = l, r
                # deduct the characters from the left index
                window_count[character] -= 1
                # once the window does not satisfy the complete subset of the target
                if character in target_count and window_count[character] < target_count[character]:
                    # reduce the number of matched frequency
                    formed -= 1
                # shrink the window size
                l += 1
        # return empty string if there is no match or return the matched substring
        return "" if ans.length == float("inf") else s[ans.left : ans.right + 1]