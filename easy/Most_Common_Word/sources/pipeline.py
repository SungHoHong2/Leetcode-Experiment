class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # replace the punctuations with spaces,
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        # split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        # count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # return the word with the highest frequency
        rtnStr = None
        value = float("-inf")
        for key, val in word_count.items():
            # print(key, val)
            if value < val:
                value = val
                rtnStr = key

        return rtnStr