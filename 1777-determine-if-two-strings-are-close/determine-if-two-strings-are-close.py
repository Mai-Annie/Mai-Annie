class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #Check if the words are the same length
        if len(word1) != len(word2):
            return False

        #Track the unique characters in each word
        chars1 = set(word1)
        chars2 = set(word2)

        #Create frequency maps for each word
        frequency_word1 = {}
        frequency_word2 = {}
        for char in word1:
            if char in frequency_word1:
                frequency_word1[char] += 1
            else:
                frequency_word1[char] = 1

        for char in word2:
            if char in frequency_word2:
                frequency_word2[char] += 1
            else:
                frequency_word2[char] = 1

        if chars1 == chars2:  #Check if set of characters in each word is the same
            return sorted(frequency_word1.values()) == sorted(frequency_word2.values()) #check if frequencies of words are the same 
        else:
            return False