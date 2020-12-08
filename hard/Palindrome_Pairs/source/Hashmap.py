class Solution:

    def all_valid_prefixes(self, word):
        # set the array to collect substrings that can be compared with word2
        valid_prefixes = []
        # iterate the word1
        for i in range(len(word)):
            # if there are palindrome within the rightside of word1
            if word[i:] == word[i:][::-1]:
                # return the lefovers that can be compared with word2
                valid_prefixes.append(word[:i])
        return valid_prefixes

    def all_valid_suffixes(self, word):
        # set the array to collect available substrings that can be compared with word1
        valid_suffixes = []
        # iterate the word2
        for i in range(len(word)):
            # if there are palindrome within the leftside of word2
            if word[:i + 1] == word[:i + 1][::-1]:
                # return the leftovers that can be compared with word1
                valid_suffixes.append(word[i + 1:])
        # return the availble substrings
        return valid_suffixes

    def palindromePairs(self, words):
        # set the hashmap that stores the indexes of each word
        word_lookup = {word: i for i, word in enumerate(words)}
        # set the array to store the possible pairs
        solutions = []

        # iterate the input
        for word_index, word in enumerate(words):
            # get the reversed word
            reversed_word = word[::-1]
            # case #1
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])

            # case #2
            for suffix in self.all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # case #3
            for prefix in self.all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])

        # return the available pairs
        return solutions