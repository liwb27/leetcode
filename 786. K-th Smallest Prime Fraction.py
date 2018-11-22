# A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.

# Input: A = [1, 7], K = 1
# Output: [1, 7]
# Note:

# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.

# from queue import PriorityQueue
import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        count = 1
        length = len(A)#smallest is A[0]/A[j]

        # que = PriorityQueue()
        que = []

        heapq.heappush(que, (A[0]/A[length-1], (0, 0)))
        # que.put((A[0]/A[length-1], (0, 0)))# 先放入第一列

        while count <= K:
            count = count + 1
                
            (val, (i, j)) = heapq.heappop(que)
            # (val, (i, j)) = que.get()
            # print(val, str(A[j])+'/'+str(A[length-1-i]))
            if i+1 < length: #向下
                heapq.heappush(que, (A[j]/ A[length-2-i], (i+1, j)))
                # que.put((A[j]/ A[length-2-i], (i+1, j)))
            if j+1 < length and i==0: # 向右
                heapq.heappush(que, (A[j+1] / A[length-1-i], (i, j+1)))
                # que.put((A[j+1] / A[length-1-i], (i, j+1))) # 左下
        return [A[j],A[length-1-i]]
        

# A=  [1,3,5,7,11]
#   11 1/11, 3/11,...
#   7  1/7, ...
#   5  1/5, ...
#   3
#   1
# 转化为no. 378 问题
# 用priorityque会不通过，改用heap可以通过...
            

print(Solution().kthSmallestPrimeFraction([1,3,5,7,11],5))