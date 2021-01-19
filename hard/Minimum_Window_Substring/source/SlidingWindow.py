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
        # set a hashmap that counts the frequency of the unique characters of the target
        target_count = collections.defaultdict(int)
        for c in t:
            target_count[c] += 1
        # keep track of number of characters of target that are matched with input
        target_matched = 0
        # set a hashmap that counts the frequency of the unique characters of the current window
        window_count = collections.defaultdict(int)
        # set a returning tuple (window length, left, right)
        ans = Window(float('inf'), None, None)
        # set the left and right pointer
        left, right = 0, 0
        # start expanding the window from the right
        for right in range(len(s)):
            # get the new character from the right
            char = s[right]
            # add to the map
            window_count[char] += 1
            # check if the frequency of the character in the window matches with the target
            if char in target_count and window_count[char] == target_count[char]:
                target_matched += 1
            # start shrinking the window from the left once it contains the substring of the target
            while left <= right and target_matched == len(target_count):
                # get the old character from the left
                char = s[left]
                # record the smallest window
                if right - left + 1 < ans.length:
                    ans.length = right - left + 1
                    ans.left, ans.right = left, right
                # deduct the characters from the left index
                window_count[char] -= 1
                # once the window does not satisfy the complete subset of the target
                if char in target_count and window_count[char] < target_count[char]:
                    # reduce the number of matched frequency
                    target_matched -= 1
                # shrink the window size
                left += 1
        # return empty string if there is no match or return the matched substring
        return "" if ans.length == float('inf') else s[ans.left:ans.right+1]