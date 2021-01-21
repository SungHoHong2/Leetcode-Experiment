class Solution:
    def validSuffixes(self, word):
        # set the array that collects word2 substring comparable to word1
        ans = list()
        # iterate the word2
        for i in range(len(word)):
            # append the rightside to the array if the leftside is a palindrome
            if word[:i + 1] == word[:i + 1][::-1]:
                ans.append(word[i + 1:])
        # return the substrings that can be compared with word1
        return ans

    def validPrefixes(self, word):
        # set the array that collects word1 substring comparable to word2
        ans = list()
        # iterate the word1
        for i in range(len(word)):
            # append the leftside to the array if the rightside is a palindrome
            if word[i:] == word[i:][::-1]:
                ans.append(word[:i])
        # return the substrings that can be compared with word2
        return ans

    def palindromePairs(self, words):
        # set the hashmap[word] = index
        wordMap = {word: i for i, word in enumerate(words)}
        # set the array to store the possible pairs
        ans = list()
        # iterate the input
        for idx, word in enumerate(words):
            # get the reversed word
            reverse = word[::-1]
            # case1: both words are palindrome to each other
            if reverse in wordMap and idx != wordMap[reverse]:
                ans.append([idx, wordMap[reverse]])
                # case2: if word1 is shorter than word2
            for suffix in self.validSuffixes(word):
                reverse = suffix[::-1]
                if reverse in wordMap:
                    ans.append([wordMap[reverse], idx])
                    # case3: if word1 is longer than word2
            for prefix in self.validPrefixes(word):
                reverse = prefix[::-1]
                if reverse in wordMap:
                    ans.append([idx, wordMap[reverse]])
                    # return the available pairs
        return ans