# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        right_flag = True
        left_flag = True
        while True:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
                if right <= left:
                    return True
            else:
                if left_flag:
                    if right_flag:
                        record_right = right
                        record_left = left
                    else:
                        right = record_right
                        left = record_left
                    left_flag = False
                    left = left+1
                elif right_flag:
                    if left_flag:
                        record_right = right
                        record_left = left
                    else:
                        right = record_right
                        left = record_left
                    right = right-1
                    right_flag = False
                else:
                    return False



    def validPalindrome2(self, s): # 速度太慢
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            n = len(s)
            for i in range(int(n/2) + 1):
                if s[i] != s[n-i-1]:
                    return False
            return True

        for i in range(len(s)):
            s2 = s[:i] + s[i+1:]
            if isPalindrome(s2):
                return True
        return False

print(Solution().validPalindrome("ebcbbececabbacecbbcbe"))
