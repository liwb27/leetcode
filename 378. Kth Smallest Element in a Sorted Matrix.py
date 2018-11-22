# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.

from queue import PriorityQueue

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 1
        i = 0
        i_max = len(matrix)
        if i_max == 0:
            return None
        j = 0
        j_max = len(matrix[0])
        if j_max == 0:
            return None

        que = PriorityQueue()
        for i in range(i_max):
            que.put((matrix[i][0], (i, 0)))# 先放入第一列

        while count <= k:
            count = count + 1
            if que.empty():
                return None # error
            (val, (i, j)) = que.get()
            if j+1 < j_max: # 向右
                que.put((matrix[i][j+1], (i, j+1)))
        return matrix[i][j]


    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 1
        i = 0
        i_max = len(matrix)
        if i_max == 0:
            return None
        j = 0
        j_max = len(matrix[0])
        if j_max == 0:
            return None

        que = PriorityQueue()
        que.put((matrix[i][j], (i, j)))# 坐上角元素最小

        while count <= k:
            count = count + 1
            if que.empty():
                return None # error
            (val, (i, j)) = que.get()
            # print(val)
            if i+1 < i_max: #向下
                que.put((matrix[i+1][j], (i+1, j)))
            if j+1 < j_max and i==0: # 向右，只有第一行可以向右
                que.put((matrix[i][j+1], (i, j+1))) # 左下
        return matrix[i][j]
k = 3
A = [[1,5,9],[10,11,13],[12,13,15]]
print('result=', Solution().kthSmallest(A, k))