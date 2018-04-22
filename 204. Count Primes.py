# Description:

# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        prime = [True] * n
        prime[:2] = [False, False]
        for base in xrange(2, int((n - 1) ** 0.5) + 1):
            if prime[base]:
                prime[base ** 2::base] = [False] * len(prime[base ** 2::base])
        return sum(prime)