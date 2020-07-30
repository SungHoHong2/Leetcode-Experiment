class Solution(object):
    def isAlienSorted(self, words, order):
        # set the hashmap that records the key as the char and the value as the order
        order_index = {c: i for i, c in enumerate(order)}
        # iterate the words
        for i in range(len(words) - 1):
            # get the first word
            word1 = words[i]
            # get the second word
            word2 = words[i+1]
            # set a flag for identical words
            identical = True
            # iterate the shortest word
            for k in range(min(len(word1), len(word2))):
                # if the characters are not identical
                if word1[k] != word2[k]:
                    # if the order of the characters are wrong
                    if order_index[word1[k]] > order_index[word2[k]]:
                        # return false
                        return False
                    # if the order is correct
                    else:
                        # the word is not identical and don't need to compare anymore
                        identical = False
                        break
            # if the word is identical but the length of the first word is longe
            if identical and len(word1) > len(word2):
                # return false
                return False
        # return true if there is no problems
        return True