class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght_substring = {}
        word = []
        for letter in s:
            if letter not in word:
                word.append(letter)
            else:
                lenght_substring[len(word)] = word
                to_dell = word.index(letter) + 1
                word = word[to_dell:]
                word.append(letter)
        key = len(word)
        if len(lenght_substring) >= 1:
            v = max(lenght_substring.keys())
            key = v if key < v else key
        return key

#88% SPEED, in working to upgrade
