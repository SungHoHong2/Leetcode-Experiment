class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        # iterate each character from the paragraph
        for p, char in enumerate(paragraph):

            # word_buffer = a word from the paragraph
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph) - 1:
                    continue

            # begin processing one word
            if len(word_buffer) > 0:
                # get the string
                word = "".join(word_buffer)
                # if the word is not part of the banned_words
                if word not in banned_words:
                    # increase the number
                    word_count[word] += 1
                    # if the total cound exceeds the max_count
                    if word_count[word] > max_count:
                        # update the return answer
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans