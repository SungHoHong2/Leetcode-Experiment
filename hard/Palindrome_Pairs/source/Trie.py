class TrieNode:
    def __init__(self):
        # set the pointer for trienode
        self.next = collections.defaultdict(TrieNode)
        # set the indexes of the each word
        self.ending_word = -1
        # set a mark for palindromes
        self.palindrome_suffixes = []

class Solution:
    def palindromePairs(self, words):
        # Create the Trie
        trie = TrieNode()
        # add the reversed nodes in the Trie
        for i, word in enumerate(words):
            word = word[::-1]
            current_level = trie
            for j, c in enumerate(word):
                # Label the the remainder if they are a palindrome.
                if word[j:] == word[j:][::-1]:
                    current_level.palindrome_suffixes.append(i)
                current_level = current_level.next[c]
            # mark the current level with the current word
            current_level.ending_word = i

        # Look up each word in the Trie and find palindrome pairs.
        solutions = []
        for i, word in enumerate(words):
            current_level = trie
            # case 3: if word1 is longer than word2
            for j, c in enumerate(word):
                # if a matching word is found in the current level
                if current_level.ending_word != -1:
                    # check the rightside of word1 is a palindrome
                    if word[j:] == word[j:][::-1]:
                        # add as a solution
                        solutions.append([i, current_level.ending_word])
                # break if no matching word is found
                if c not in current_level.next:
                    break
                # go down to the deeper level of Trie
                current_level = current_level.next[c]
            # if case 3 is not applied after iterating teh whole word
            else:
                # case 1: a palindrome is found
                if current_level.ending_word != -1 and current_level.ending_word != i:
                    solutions.append([i, current_level.ending_word])
                # case 2: if word2 is longer than word1 and word2 consists a palindrome
                for j in current_level.palindrome_suffixes:
                    solutions.append([i, j])
        # return the palindrome pairs
        return solutions