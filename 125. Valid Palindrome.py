# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

def is_palindrome(word):
    return word==word[::-1]

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == '':
            return True
        # ss = ''
        # for i in s:
        #     if i.isalnum():
        #         ss.join(i.lower())
        ss = ''.join([x.lower() for x in s if x.isalnum()])
        return ss==ss[::-1]




print(Solution().isPalindrome('0P'))