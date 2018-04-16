# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def confilct(state, nextX):
            nextY = len(state)
            for i in range(nextY):
                if abs(state[i]-nextX) in (0, nextY-i):
                    return True
            return False    

        def queens(num=8, state=()):
            for pos in range(num):
                if not confilct(state, pos):
                    if len(state) == num-1:
                        yield (pos,)
                    else:
                        for result in queens(num, state + (pos,)):
                            yield (pos,) + result
        return len(list(queens(n)))