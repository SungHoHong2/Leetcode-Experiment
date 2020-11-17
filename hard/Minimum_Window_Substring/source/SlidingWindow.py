class Solution:
    def minWindow(self, s, t):
        # return empty string if the input is invalid
        if not t or not s:
            return ""
        # declare a hashmap that counts the frequency of the unqiue characters of string "t"
        dict_t = collections.defaultdict(int)
        for c in t:
            dict_t[c] += 1
        # get the total number of unique characters of string "t"
        required = len(dict_t)
        # left and right pointer
        l, r = 0, 0
        # keep track of number of characters of string "t" that are matched with string "s"
        formed = 0
        # declare a hashmap that counts the frequency of the unqiue characters of the current window
        window_counts = collections.defaultdict(int)
        # delcare a tuple of the form (window length, left, right)
        ans = (float("inf"), None, None)
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            # add to the map
            window_counts[character] += 1
            # check if the frequency of the character in the window matchs with the string "t"
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # start recording the answer once the window contains the substring of "t"
            while l <= r and formed == required:
                character = s[l]
                # record the smallest window
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # deduct the characters from the left index
                window_counts[character] -= 1
                # once the window does not satisfy the complete subset of string "t"
                if character in dict_t and window_counts[character] < dict_t[character]:
                    # reduce the number of matched frequency
                    formed -= 1
                # shrink the window size
                l += 1
            # increase the window size
            r += 1
        # return empty string if there is no match or return the matched substring
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]