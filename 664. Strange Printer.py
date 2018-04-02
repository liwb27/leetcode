# There is a strange printer with the following two special requirements:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
# Hint: Length of the given string will not exceed 100.

# 需要按顺序输出所有的字符，打印机每次可以从任意位置开始输出任意多个相同字符，并且后输出的字符会覆盖前面
# 例如'aba': 先输出aaa，然后从第二个位置开始输出b，2次就可以输出完成
# 题目需要求用最少的次数输出完成
import random

class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = {}
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            else:
                if (i,j) not in moves:
                    min_answer = 1 + dp(i+1, j) # 如果s[i+1,j]中没有和s[i]相同时的结果
                    for k in range(i+1,j+1): #第一步从i输出到k，跳过第一个
                        if s[i] == s[k]: #i和k必须一致
                            n = k+1
                            for n in range(k+1,j): #找出从k向后所有相同的字母，并跳过
                                if s[n] != s[k]:
                                    break
                            ans = dp(i+1, k) + dp(n, j) #从的一个和s[i]不同的字母开始计算
                            if ans < min_answer:
                                min_answer = ans
                    moves[i,j] = min_answer
                    return min_answer
                else:
                    return moves[i,j]


        return dp(0, len(s)-1)        


if __name__ == '__main__':
    # available_string = 'abcdefghijklmnopqrstuvwxyz'
    available_string = 'abcdef'
    test_string = ''.join(random.choice(available_string) for _ in range(80))
    print(test_string)
    print(Solution().strangePrinter(test_string))