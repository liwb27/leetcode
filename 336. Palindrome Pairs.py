# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[-(i+1)]:
            return False
    return True

class Solution:
    # 最直接做法，超时
    def palindromePairs2(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        pairs = []
        for i in range(len(words)):
            word1 = words[i]
            for j in range(i+1, len(words)):
                word2 = words[j]
                if is_palindrome(word1+word2):
                    pairs.append([i, j])
                if is_palindrome(word2+word1):
                    pairs.append([j, i])
        return pairs

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        words = {word: i for i, word in enumerate(words)}
        pairs = []
        for word in words:
            i = words[word]
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if is_palindrome(prefix):
                    suffix_back = suffix[::-1]
                    if suffix_back != word and suffix_back in words:
                        pairs.append([words[suffix_back], i])
                if is_palindrome(suffix) and j != len(word):
                    prefix_back = prefix[::-1]
                    if prefix_back != word and prefix_back in words:
                        pairs.append([i, words[prefix_back]])
        return pairs

print(Solution().palindromePairs(['asdlk','sdaf']))