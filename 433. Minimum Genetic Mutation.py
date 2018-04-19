# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

# Note:

# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# Example 1:

# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]

# return: 1
# Example 2:

# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

# return: 2
# Example 3:

# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

# return: 3

def canMutation(s1, s2):
    count = 0
    index = -1
    for i in range(len(s1)):
        if s1[i] != s2[i]: #找到不同位置
            count += 1
    return count == 1

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """           
        if start == end:
            return 0
        start_set = set([start])
        bank_set = set(bank) - start_set
        if end not in bank:
            return -1
        start_set2 = set()
        count = 0
        while bank_set: # 剩余数为0时，无可用突变
            for item in start_set: #与end比较
                if canMutation(item, end):#能否突变
                    return count+1 #返回计数
            count += 1 # 记录突变次数
            for s1 in start_set: #比较start和bank，判断从start可以突变为那些值
                for s2 in bank_set:
                    if canMutation(s1, s2):
                        start_set2.add(s2) #记录可突变值
            if len(start_set2) == 0: #没有可用突变，则无解
                return -1
            start_set = start_set2
            bank_set = bank_set - start_set2
            start_set2 = set()
        return -1

if __name__ == '__main__':
    # start = "AACCGGTT"
    # end =  "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    start = "AAAAAAAA"
    end =  "CCCCCCCC"
    bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
    
    print(Solution().minMutation(start, end, bank))