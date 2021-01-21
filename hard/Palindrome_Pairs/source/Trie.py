class TrieNode:
    def __init__(self):
        # set the pointer to the next level
        self.next = collections.defaultdict(TrieNode)
        # set the indicator that the current level is a finished word
        self.word_index = -1
        # set the indicator that the current level is a palindrome
        self.palindrome = list()

class Solution:
    """
    case1: [CAT] [TAC]
    case2: [CAT] [SOLOS TAC]
    case3: [CAT SOLOS] [TAC]
    """
    def palindromePairs(self, words):
        # create the Trie
        trie = TrieNode()
        # iterate the words
        for i, word in enumerate(words):
            # reverse the word
            word = word[::-1]
            # set the pointer to the current level of the trie
            curr = trie
            # iterate the chars from the word
            for j, c in enumerate(word):
                # label the index of the word if the word is a palindrome
                if word[j:] == word[j:][::-1]:
                    curr.palindrome.append(i)
                # move down the trie to the next level
                curr = curr.next[c]
            # label the word after finish exploring the word
            curr.word_index = i

        # set the returning array
        ans = list()
        # iterate the word
        for i, word in enumerate(words):
            # set the pointer of the current level of the trie
            curr = trie
            # case3: if word1 is longer than word2
            for j, c in enumerate(word):
                # if the leftside is a word
                if curr.word_index != -1:
                    # if the rightside is a palindrome
                    if word[j:] == word[j:][::-1]:
                        # add as a solution of case3
                        ans.append([i, curr.word_index])
                # break if the word does not exist
                if c not in curr.next:
                    break
                # go down to the deeper level of Trie
                curr = curr.next[c]
            # if the entire level of the trie is a word with no case3
            else:
                # case1: the whole word is a palindrome
                if curr.word_index != -1 and curr.word_index != i:
                    ans.append([i, curr.word_index])
                # case2: leftside is a palindrome and the rightside is a word
                for j in curr.palindrome:
                    ans.append([i, j])
                    # return the palindrome pairs
        return ans
