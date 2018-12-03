# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        vals = self.parse(s, 1)
        result = []
        if vals == None:
            return []
        for val in vals:
            result.append('{0}.{1}.{2}.{3}'.format(val[0],val[1],val[2],val[3]))
        return result

    def parse(self, s, num):
        if num == 4:
            if s == '':
                return None
            if s[0] == '0' and len(s) != 1:
                return None
            p = int(s)
            if p <= 255:
                return [[None,None,None,p]]
            else:
                return None
        else:
            result = []
            if s == '':
                return None
            p1 = int(s[0])
            result1 = self.parse(s[1:],num+1)
            if result1 != None:
                for val in result1:
                    val[num-1] = p1
                result.extend(result1)
                    
            if p1 != 0:
                p2 = int(s[0:2])
                result2 = self.parse(s[2:],num+1)
                if result2 != None:
                    for val in result2:
                        val[num-1] = p2
                    result.extend(result2)

                p3 = int(s[0:3])
                if p3 <= 255 and p1 != 0:
                    result3 = self.parse(s[3:],num+1)
                    if result3 != None:
                        for val in result3:
                            val[num-1] = p3
                        result.extend(result3)

            if result != []:
                return result
            else:
                return None
            
# "010010"
# 1111
# 0000
# 001001
# "255255255255"
print(Solution().restoreIpAddresses(""))